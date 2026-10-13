
import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_api_data():
    """Fetch JSON data from a public REST API."""
    try:
        response = requests.get(API_URL, timeout=10)

        # Check the HTTP status code
        response.raise_for_status()

        # Convert JSON response into Python data
        data = response.json()

        return data

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    except json.JSONDecodeError:
        print("Error: The API returned invalid JSON.")

    return None


def display_data(data):
    """Display selected API information in a clean format."""
    if not data:
        print("No data available.")
        return

    print("\n========== API RESPONSE ==========")
    print(f"Post ID : {data.get('id', 'N/A')}")
    print(f"User ID : {data.get('userId', 'N/A')}")
    print(f"Title   : {data.get('title', 'N/A')}")
    print(f"Body    : {data.get('body', 'N/A')}")
    print("==================================")


def main():
    print("Simple Python API Client")
    print("Fetching data from the public REST API...")

    data = fetch_api_data()

    if data is not None:
        print("\nAPI request successful!")
        display_data(data)


if __name__ == "__main__":
    main()