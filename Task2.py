import csv
import json
import os
import requests
from dotenv import load_dotenv


# 1. Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API_KEY loaded successfully")
else:
    print("API_KEY not found in .env")


# 2. Read employee CSV and write employees.json
#    and high_earners.csv without storing all employees in a list

rows_read = 0
high_earners_count = 0

with open(
    "employee.csv", "r", newline="", encoding="utf-8-sig"
) as csv_file:

    reader = csv.DictReader(csv_file)

    with open("employees.json", "w", encoding="utf-8") as json_file, \
         open("high_earners.csv", "w", newline="", encoding="utf-8") as high_file:

        high_writer = csv.DictWriter(
            high_file, fieldnames=reader.fieldnames
        )
        high_writer.writeheader()

        json_file.write("[\n")
        first_row = True

        for row in reader:
            rows_read += 1

            # Convert numeric fields
            row["id"] = int(row["id"])
            row["Salary"] = int(row["Salary"])

            # Write employee to JSON array
            if not first_row:
                json_file.write(",\n")

            json.dump(row, json_file, indent=4)
            first_row = False

            # Write employees earning above 50000
            if row["Salary"] > 50000:
                high_writer.writerow(row)
                high_earners_count += 1

        json_file.write("\n]\n")


print(f"Rows read: {rows_read} | High earners: {high_earners_count}")


# 3. GET users from JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

try:
    response = requests.get(
        f"{BASE_URL}/users",
        timeout=5
    )
    response.raise_for_status()

    api_users = response.json()

    # 4. Extract nested fields using .get()
    processed_users = []

    for user in api_users:
        address = user.get("address", {})
        company = user.get("company", {})

        processed_users.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "company": company.get("name")
        })

    # Save processed API data to users.json
    with open("users.json", "w", encoding="utf-8") as json_file:
        json.dump(processed_users, json_file, indent=4)

    # Print the first 3 users
    for user in processed_users[:3]:
        print(
            f'{user["id"]} - {user["name"]} - {user["email"]}'
        )

except requests.exceptions.Timeout:
    print("API request timed out")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


# 5. Check the 404 response for /users/9999
try:
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()
        print("/users/9999 ->", response.status_code)

except requests.exceptions.Timeout:
    print("/users/9999 -> Request timed out")

except requests.exceptions.ConnectionError:
    print("/users/9999 -> Connection error")

except requests.exceptions.RequestException as error:
    print("/users/9999 -> Request failed:", error)
