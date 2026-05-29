
#!/usr/bin/env python3
# Author      : Bilal Haider ID (github.com/BilalHaiderID)
# Version     : 0.0.2
# Description : CLI tool to fetch PAK SIM owner info using phone numbers or ranges
# DISCLAIMER  : This tool is for educational and research purposes only.
#               The author is not responsible for any misuse or illegal activity.
#               Always ensure you have permission before querying personal data.

import requests, argparse, re
from bs4 import BeautifulSoup

def numinfo(mobile_number):
    try:
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0','Content-Type': 'application/x-www-form-urlencoded','Referer': 'https://google.com'}
        response = session.get(f"https://datacorporation.com.pk/sim-owner-details/?sim_info_mobile={mobile_number}")
        soup = BeautifulSoup(response.text, 'html.parser')
        card_items = soup.find_all("div", class_="sim-info-card-item")
        if len(card_items) != 0:
            for item in card_items:
                label = item.find("div", class_="sim-info-card-label").get_text(strip=True)
                value = item.find("div", class_="sim-info-card-value").get_text(strip=True)
                if str(value.strip()) != "":
                    print(f"   [+] {label}  : {value}")
        else:
            print(f"   [x] data not found for : {mobile_number}")
    except KeyboardInterrupt:exit()
    except Exception as e:print(f"[!] Error for {mobile_number}: {e}")

def expand_range(rng):
    match = re.match(r'^(\d+)-(\d+)$', rng)
    if not match:print(f"[!] Invalid range: {rng}"); return []
    start_str, end_str = match.groups()
    start, end = int(start_str), int(start_str[:-len(end_str)] + end_str)
    return [str(i) for i in range(start, end + 1)]

def main():
    parser = argparse.ArgumentParser(description="CLI tool to fetch PAK SIM owner info using phone numbers or ranges")
    parser.add_argument("-n", "--numbers", help="Comma-separated mobile numbers")
    parser.add_argument("-r", "--range", nargs="+", help="Range(s) like 03445450870-75 or -975")
    args = parser.parse_args()
    numbers = []
    if args.numbers:numbers += [n.strip() for n in args.numbers.split(",") if n.strip()]
    if args.range:
        for r in args.range:numbers += expand_range(r)
    if not numbers:print("[!] No numbers provided. Use -n or -r."); return
    for number in numbers:print(f"\n[>>] Checking: {number} : "); numinfo(number)

if __name__ == "__main__":main()
