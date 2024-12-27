# SMTP Enumeration Script

This script performs enumeration on an SMTP server using the `VRFY` command to verify the existence of usernames.

## Features
- Connects to an SMTP server on port 25.
- Uses the `VRFY` command to test usernames from a wordlist.
- Outputs the server's response for each username.

## Requirements
- Python 3.x
- An accessible SMTP server (target)
- A wordlist file (e.g., `wordlist.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smtp-enum.git
   cd smtp-enum
