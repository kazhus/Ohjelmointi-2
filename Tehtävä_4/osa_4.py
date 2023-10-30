import requests

query = input("What kind of jokes would you like? : ")
req = f"https://api.chucknorris.io/jokes/categories=q{query}"
def get_joke(show_data):

    get_joke(query)
try:
    response_content =requests.get(req).json()
    get_joke(response_content)

except requests.exceptions.RequestException as error:
    print("Network connection failed")
    print(error)