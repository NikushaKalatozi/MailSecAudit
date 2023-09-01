import dns.resolver

def check_spf(domain):
    try:
        result = dns.resolver.resolve(domain, 'TXT')
        for rdata in result:
            if "v=spf" in rdata.strings[0].decode():
                return rdata.strings[0].decode()
    except:
        return "No SPF record found."

def check_dkim(domain, selector="default"):
    try:
        result = dns.resolver.resolve(f"{selector}._domainkey.{domain}", 'TXT')
        return result[0].strings[0].decode()
    except:
        return f"No DKIM record found for selector '{selector}'."

def check_dmarc(domain):
    try:
        result = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        return result[0].strings[0].decode()
    except:
        return "No DMARC record found."

def main():
    filename = "domains.txt"  # Path to your text file with domain list

    with open(filename, "r") as file:
        domains = file.read().splitlines()

    for domain in domains:
        print(f"Domain: {domain}")
        print(f"SPF: {check_spf(domain)}")
        print(f"DKIM (default selector): {check_dkim(domain)}")
        print(f"DMARC: {check_dmarc(domain)}")
        print("\n")

if __name__ == "__main__":
    main()
