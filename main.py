import sys
import json
import requests


def get_ip() -> str:
    ip = requests.get("https://ifconfig.me").text
    return ip


def update_record(public_key: str, secret_key: str, domain: str, record: dict) -> bool:
    url = "https://api.godaddy.com/v1/domains/{}/records/{}/{}".format(domain, record["type"], record["name"])
    
    header = {
        "Authorization": "sso-key {}:{}".format(public_key, secret_key),
        "Content-Type": "application/json",
        "Host": "api.godaddy.com"
    }

    ip = get_ip()

    data = '[{"data": "%s", "ttl": %s}]' % (ip, record["ttl"])

    response = requests.put(url, data, headers=header)
    if response.text:
        print(response.text)

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <config_file>")
        sys.exit(1)
    
    with open(sys.argv[1], "r") as f:
        config = json.loads(f.read())
    
    public_key = config["public_key"]
    secret_key = config["secret_key"]
    domain = config["domain"]
    records = config["records"]

    for record in records:
        success = update_record(public_key, secret_key, domain, record)
        if not success:
            print("Failed record: " + str(record))
