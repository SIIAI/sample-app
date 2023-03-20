import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italy"
dest = "Frascati, Italy"
key = "qfQBzH9Js6MksuxdipPcHKEaWJOuJRGQ"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)