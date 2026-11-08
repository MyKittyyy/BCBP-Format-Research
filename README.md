# BCBP-Format-Research

# BCBP Format Automation & Payload Generator

## Overview

This repository contains a Python utility for generating valid **IATA BCBP (Bar Coded Boarding Pass)** data structures. It is designed for security researchers, developers, and aviation enthusiasts who need to understand, test, or automate the generation of BCBP formatted strings.

The tool focuses on the mathematical and structural rules defined in **IATA Resolution 792**, automating the creation of mandatory, unique, and repeated fields, as well as the critical hexadecimal length calculations required for the conditional (variable) section.

## Why This Tool?

Manually constructing a valid BCBP string is error-prone and time-consuming. The format enforces strict character offsets, specific document types (e.g., 'B' for boarding pass), and hexadecimal length values for the variable section. This script eliminates human error by programmatically building the payload according to the standard.

It is particularly useful for:
- Security testing of systems that parse BCBP data.
- Understanding the validation logic and error handling of BCBP parsers (Error Oracle techniques).
- Automating the generation of test data for aviation-related applications.

## Features

- **Automated Field Construction:** Builds the mandatory (58 characters), unique, and repeated sections according to IATA specifications.
- **Dynamic Hexadecimal Calculation:** Automatically calculates the `Item 6` (variable field size) in hexadecimal, ensuring the conditional section is correctly framed.
- **Customizable Payload Injection:** Allows the user to specify custom data (e.g., SQL payloads, test strings) for the `airline_use` field, which is often the least validated part of the format.
- **Length Validation:** Includes assertions to ensure each section meets the required character length, preventing truncation errors.

## Usage

```bash
python3 build_bcbp.py "YOUR_PAYLOAD_HERE"
