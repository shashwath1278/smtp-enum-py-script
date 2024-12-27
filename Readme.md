# SMTP Enumeration Script

This repository contains a Python script for enumerating usernames on an SMTP server using the `VRFY` command. The script reads usernames from a wordlist file, attempts to verify them on the target SMTP server, and outputs the server's response for each username.

## Features
- Connects to an SMTP server on port 25.
- Uses the `VRFY` command to test usernames from a wordlist.
- Displays the response code and message for each tested username.
- Simple and easy-to-use interface.

## Requirements
- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Wordlist file**: A text file containing usernames to test, with one username per line.
- **SMTP server**: A reachable target SMTP server that supports the `VRFY` command.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/smtp-enum.git
   cd smtp-enum
   ```

2. Verify that Python 3.x is installed:
   ```bash
   python3 --version
   ```

3. (Optional) Create a virtual environment to isolate dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate    # On Windows
   ```

## Usage
1. Prepare a wordlist file (`wordlist.txt`) with the usernames you want to test, with one username per line.
2. Run the script:
   ```bash
   python3 smtp_enum.py
   ```
3. Provide the required inputs when prompted:
   ```plaintext
   Target IP or hostname: <target-ip>
   Format: wordlist.txt (assuming wordlist is in the same directory as the script): wordlist.txt
   ```

### Example Wordlist
```plaintext
admin
user
root
test
guest
```

### Example Output
If the target SMTP server supports the `VRFY` command:
```plaintext
Response for admin: 252 2.0.0 admin@target-domain.com
Response for test: 550 5.1.1 User unknown
Response for user: 252 2.0.0 user@target-domain.com
```

If there is an error (e.g., connection issues or `VRFY` disabled):
```plaintext
Error with admin: [Errno 111] Connection refused
Error with test: SMTPServerDisconnected: Connection unexpectedly closed
```

## Notes
- The script assumes the target SMTP server supports the `VRFY` command. Some modern SMTP servers disable this command for security reasons.
- Ensure you have explicit permission to test the target SMTP server to comply with ethical and legal guidelines.
- To avoid hanging, the script includes a timeout for server responses.

## Troubleshooting

1. **Check Connectivity to the SMTP Server:**
   Use `telnet` or `nc` to confirm the server is reachable:
   ```bash
   telnet <target-ip> 25
   ```

2. **Enable Debugging:**
   Modify the script to include print statements to debug where it hangs or fails.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features. Suggestions and feedback are welcome!

## Disclaimer
This script is intended for educational and authorized security testing purposes only. Unauthorized use of this tool against systems you do not own or have explicit permission to test is illegal and unethical.

