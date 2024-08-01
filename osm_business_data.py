import requests
import overpy
import geojson
import pandas as pd

# Dictionary of predefined regions
predefined_regions = {
    "new_york_city": "40.7128,-74.0060,40.7749,-73.9125",
    "los_angeles": "34.0522,-118.4442,34.0738,-118.3953",
    # ... add more regions
}

def get_business_data(region_or_bbox):
  # ... your existing code ...

def list_predefined_regions():
  print("Predefined regions:")
  for region in predefined_regions:
    print(f"- {region}")

def extract_business_data(data):
  # ... your existing code ...
  for business in businesses:
    business['size'] = business['tags'].get('size', None)  # Extract size tag

  df = pd.DataFrame(businesses)
  df = df.sort_values(by='size', ascending=False)
  return df

def main():
  list_predefined_regions()
  region = input("Enter a predefined region: ")
  if region in predefined_regions:
    businesses = get_business_data(region)
    df = extract_business_data(businesses)
    print(df)
  else:
    print("Invalid region")

if __name__ == "__main__":
  main()
