import json
from azure.cosmos import CosmosClient, PartitionKey

client = CosmosClient(url="https://f1469f37-0ee0-4-231-b9ee.documents.azure.com:443/", credential="LThYZdQ1V71KXgalEr6svUgN5KBxvuIIZk9Y7UREyKbu93lXysMuEZbGAVCVcInQ3MeIIZkyJohJACDbEXgicQ==")
database = client.create_database_if_not_exists(id="stefidb")
partitionKeyPath = PartitionKey(path="/partdb")
container = database.create_container_if_not_exists(
    id="dbcontainer", partition_key=partitionKeyPath, offer_throughput=400
)

newItem = {
    "id": "70b63682-b93a-4c77-aad2-65501000265f",
    "Airport": {
      "Code": "LAX",
      "Name": "Los Angeles International Airport"
    },
    "Time": {
      "Label": "2022/11",
      "Month": 11,
      "Month Name": "November",
      "Year": 2022
    },
    "Statistics": {
      "# of Delays": {
        "Carrier": 900,
        "Late Aircraft": 925,
        "National Aviation System": 3000,
        "Security": 10,
        "Weather": 200
      },
      "Carriers": {
        "Names": "American Airlines Inc., Delta",
        "Total": 2
      },
      "Flights": {
        "Cancelled": 200,
        "Delayed": 6000,
        "Diverted": 25,
        "On Time": 20000,
        "Total": 26225
      },
      "Minutes Delayed": {
        "Carrier": 60000,
        "Late Aircraft": 40000,
        "National Aviation System": 100000,
        "Security": 400,
        "Total": 200400,
        "Weather": 20000
      }
    }
}

# container.create_item(newItem)

QUERY = "SELECT * FROM c WHERE c.id = @airportId"
params = [dict(name="@airportId", value="f117e9e0-3e27-4466-b29f-8e1a2567d43f")]

items = container.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=True
)

for item in items:
    print(json.dumps(item, indent=True))