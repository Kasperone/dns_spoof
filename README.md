
# DNS Spoofer

This is a Python script that demonstrates DNS spoofing by intercepting and modifying DNS responses on a Linux system. It is useful for educational purposes to understand how attackers manipulate DNS responses to redirect traffic to malicious servers.

## Features
- Intercepts DNS requests using a Netfilter queue.
- Modifies DNS responses to redirect traffic for specific domains.
- Demonstrates the basics of DNS spoofing with Scapy and Netfilter.

## Prerequisites
- Python 3.x
- Linux-based operating system
- `scapy` library (for handling network packets)
- `netfilterqueue` library (for working with Netfilter queues)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/dns_spoofer.git
cd dns_spoofer
```

Install the required libraries:

```bash
pip install scapy netfilterqueue
```

## Usage

Run the script with superuser privileges to enable DNS spoofing.

```bash
sudo python3 dns_spoofer.py
```

### Notes:
- Replace `XX.X.X.XX` in the script with the IP address to which you want to redirect the target domain (e.g., the attacker's server or another IP).
- Ensure that the appropriate Netfilter rules are applied to redirect traffic to the Netfilter queue.

### Setting Up Netfilter Rules:

Use the following command to redirect DNS traffic to the Netfilter queue:

```bash
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
```

If you are testing on your own machine, use:

```bash
sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
sudo iptables -I INPUT -j NFQUEUE --queue-num 0
```

### Stopping the Script:

When you are done, reset the iptables rules:

```bash
sudo iptables --flush
```

## Example:

Run the script to spoof DNS responses for `www.bing.com`. Replace the spoofed IP in the script to redirect traffic.

```bash
sudo python3 dns_spoofer.py
```

Output:

```
[+] Spoofing target
```

## Notes:
- This script is for educational purposes only. Use it responsibly and only in environments where you have permission to perform testing.
- DNS spoofing is illegal and unethical if performed without authorization.

## Troubleshooting:
- Ensure you have the required libraries installed.
- Verify that the Netfilter rules are applied correctly.
- Make sure to run the script with `sudo` or as root to access network packets.
- The target domain must match exactly (e.g., `www.bing.com` and not `bing.com`).

## License
This project is licensed under the MIT License.

## About

This script is part of the course [Learn Python & Ethical Hacking from Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/) on Udemy. The course covers Python scripting and its application in ethical hacking, network security, and more.