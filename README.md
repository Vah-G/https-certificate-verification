# HTTPS Connection and Certificate Verification

This project demonstrates practical verification of HTTPS connections
by analyzing X.509 certificates and certificate fingerprints in order
to detect potential Man-In-The-Middle (MITM) attacks.

## Objective
To study how HTTPS trust works in practice, understand browser trust
stores, and verify website certificates using OpenSSL.

## Project Description
During this project, HTTPS certificates were retrieved from real
websites and analyzed to verify their authenticity and integrity.

The focus was placed on:
- Browser-trusted Root Certificate Authorities (CAs)
- Certificate chains
- SHA-1 and SHA-256 certificate fingerprints
- Detection of potential MITM or HTTPS proxy interference

## Tools Used
- Kali Linux
- OpenSSL
- Firefox / Chrome

## Process

### 1. Reviewing Trusted Root Certificates
The list of trusted Root Certificate Authorities was reviewed in
Firefox and Chrome to understand how browsers establish HTTPS trust.

### 2. Retrieving Website Certificates
Certificates were retrieved directly from a website using OpenSSL:

```bash
openssl s_client -connect www.cisco.com:443 -servername www.cisco.com -showcerts
```
This command was used to obtain the full certificate chain presented
by the server.

### 3. Fingerprint Calculation
- SHA-1 and SHA-256 fingerprints were calculated for the retrieved
  certificates using OpenSSL tools.

### 4. Verification
- The calculated fingerprints were compared with reference values
  obtained from trusted sources and browser certificate viewers.

### 5. Browser-Based Verification
- For additional confirmation and visualization, browser GUI tools
  were used to view certificate details and fingerprints.

## Results
- No MITM or HTTPS proxy was detected
- The HTTPS connection was verified as trusted
- Certificate fingerprints matched expected values

## Notes
- All tasks were performed on a local PC
- A dedicated security workstation VM was not used
- Browser GUI tools were used for convenience and visualization

## Additional Files

- **openssl-notes.md** – detailed notes of the certificate retrieval process, 
  including SHA-1 and SHA-256 fingerprint calculations and browser verification.
  
- **fingerprint_check.py** – a simple Python script to compare SHA-1 and 
  SHA-256 fingerprints obtained via OpenSSL and the browser. 
  Returns a boolean result indicating whether the fingerprints match.

## What I Learned
- How HTTPS trust is built using Root Certificate Authorities
- How to retrieve and analyze X.509 certificates with OpenSSL
- How certificate fingerprints help detect MITM attacks
- Practical differences between SHA-1 and SHA-256 fingerprints
- How browsers validate HTTPS connections internally
