# lib/GetRequester.py
import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL passed on initialization
        and returns the body of the response as raw bytes.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content  # return bytes, not string

    def load_json(self):
        """
        Uses get_response_body to send a request,
        then returns the parsed JSON data as a Python dict or list.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
