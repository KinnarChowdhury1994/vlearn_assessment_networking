import requests
import time
from tabulate import tabulate

def check_subdomains_status(subdomains, domain):
    """
    Function to check the status of subdomains.

    Args:
    - subdomains (list): List of subdomains to be checked
    - domain (str): Domain name

    Returns:
    - resp (dict): Dictionary containing status of each subdomain
    """
    resp = {}
    for subdomain in subdomains:
        httpsUrl = f"https://{subdomain}.{domain}"
        httpUrl = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(httpsUrl)
            if response.status_code == 200:
                status = "UP"
            else:
                response = requests.get(httpUrl)
                if response.status_code == 200:
                    status = "UP"
                else:
                    status = "DOWN"
        except requests.ConnectionError:
            status = "DOWN"
        resp[subdomain] = status
    return resp

def print_status_table(resp):
    """
    Function to print status table.

    Args:
    - resp (dict): Dictionary containing status of subdomains
    """
    headers = ["Subdomain", "Status"]
    data = [[subdomain, status] for subdomain, status in resp.items()]
    print(tabulate(data, headers=headers))

def main(subdomains):
    """
    Main function to continuously check and print subdomain status.

    Args:
    - subdomains (list): List of subdomains to be checked
    """
    domain = input("Enter the domain name: ")
    print(f"Checking status for domain: {domain}")

    while True:
        resp = check_subdomains_status(subdomains, domain)
        print("\nCurrent Status:")
        print_status_table(resp)
        time.sleep(60)

if __name__ == "__main__":
    # Define the list of subdomains
    subdomains = [
                    "www",
                    "mail",
                    "blog",
                    "shop",
                    "forum",
                    "api",
                    "dev",
                    "test",
                    "admin",
                    "cdn",
                    "support",
                    "store",
                    "login",
                    "dashboard",
                    "download",
                    "status",
                    "calendar",
                    "docs",
                    "hrms",
                    "report",
                    "reports"
    # Add more subdomains as needed
]

    # Run the main function
    main(subdomains)
