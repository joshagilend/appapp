import os
from cloudflare import Cloudflare

# Initialize the Cloudflare client
client = Cloudflare(
    api_email=os.environ.get("CLOUDFLARE_EMAIL"),
    api_key=os.environ.get("CLOUDFLARE_API_KEY"),
)

# Replace with your actual zone ID
zone_id = 'your_zone_id'

# Retrieve DNS records for the zone
dns_records = client.zones.dns_records.list(zone_id=zone_id)

# Print details of each DNS record
for record in dns_records:
    print(f"Type: {record.type}, Name: {record.name}, Content: {record.content}")
