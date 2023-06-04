import argparse
import requests
from colorama import Fore
import os

r=Fore.RED
w=Fore.RESET
g=Fore.GREEN
c=Fore.CYAN
y=Fore.YELLOW

os.system("clear")

# Create the argument parser
print(f"""{r}
 ._..__   .___..__ .__. __ .  ..___.__
  | [__)    |  [__)[__]/  `|_/ [__ [__)
 _|_|       |  |  \|  |\__.|  \[___|  \.
{w}""")
parser = argparse.ArgumentParser(description='Track IP location.')

# Add the argument for IP address
parser.add_argument('--ip', type=str, help='The IP address to track')

# Parse the arguments from the command line
args = parser.parse_args()

# Check if the IP address argument is provided
if args.ip:
    ip_address = args.ip
else:
    print("IP address is required. Please provide the IP address using the -i or --ip option.")
    exit(1)

# Make an HTTP request to retrieve location data from the IP-API service
response = requests.get(f"http://ip-api.com/json/{ip_address}")

# Check if the request was successful
if response.status_code != 200:
    print("Failed to track IP location.")
else:
    data = response.json()

    # Check if the IP address was found
    if data['status'] == 'fail':
        print("IP address not found.")
    else:
        # Extract location information from the JSON response
        city = data['city']
        region = data['regionName']
        country = data['country']
        zip_code = data['zip']
        lat = data['lat']
        lon = data['lon']
        isp = data['isp']

        # Display the complete location information
        print("+----------------------------------------")
        print(f"| {y}IP Location Information{w}: {g}{ip_address}{w}")
        print("+----------------------------------------")
        print(f"[{g}+{w}] {c}City{w}: {city}")
        print(f"[{g}+{w}] {c}Region{w}: {region}")
        print(f"[{g}+{w}] {c}Country{w}: {country}")
        print(f"[{g}+{w}] {c}ZIP Code{w}: {zip_code}")
        print(f"[{g}+{w}] {c}Coordinates{w}: {lat}, {lon}")
        print(f"[{g}+{w}] {c}ISP{w}: {isp}")
        print("+----------------------------------------")