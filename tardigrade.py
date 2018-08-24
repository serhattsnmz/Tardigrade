import requests
import json
import re
import argparse

from pprint import pprint
from prettytable import PrettyTable

class Parse:

    def __init__(self):
        self.args = ""
        self.subdomains = []
        self.linkler = []
        self.result = []

        self.parse_args()
        self.read_subdomains()
        self.parse()

    def parse_args(self):
        parser = argparse.ArgumentParser(description="Fetch and try all the links in a url address.")
        parser.add_argument("-d", "--domain", metavar="", required=True, help="Domain name")
        parser.add_argument("-t", "--text", metavar="", required=True, help="Subdomain file", )
        parser.add_argument("-v", "--verbose", default="False", choices=("True", "False"), metavar="", help="See the results in real time")
        parser.add_argument("-s", "--savefile", default="False", choices=("True", "False"), metavar="", help="Save result to json file")
        self.args = parser.parse_args()

    def parse(self):
        site = "http://" + str(self.args.domain).replace("http://", "").replace("https://", "")
        print(site)
        r = requests.get(site)
        
        pattern = "[a-zA-Z0-9-_]+\.com|[a-zA-Z0-9-_]+\.net|[a-zA-Z0-9-_]+\.org"
        regex = re.compile(pattern)
        self.linkler = list(set(regex.findall(r.text)))

    def read_subdomains(self):
        with open(self.args.text) as f:
            self.subdomains = f.read().split("\n")

    def try_subdomains(self):
        for link in self.linkler:
            for sub in self.subdomains:
                domain = f"http://{sub}.{link}"
                try:
                    r = requests.get(domain, stream=True)
                    if r.status_code == 200:
                        self.result.append({
                            "ip_address" : r.raw._connection.sock.getpeername()[0],
                            "domain_name" : domain
                        })
                        if self.args.verbose == "True":
                            print("Connection : " + domain)
                except:
                    if self.args.verbose == "True":
                        print("Error : " + domain)

    def save_file(self):
        if self.args.savefile == "True":
            with open("result.json", "w") as f:
                json.dump(self.result, f)
                print("File created.")

    def write_result(self):
        p = PrettyTable()
        p.field_names = ["Domain Name", "IP Address"]
        for res in self.result:
            p.add_row([res["domain_name"],res["ip_address"]])
        print(p)


if __name__ == "__main__":
    p = Parse()
    p.try_subdomains()
    p.write_result()
    p.save_file()