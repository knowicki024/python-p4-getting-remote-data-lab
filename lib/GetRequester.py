import requests
import json

class GetRequester:

    def __init__(self, url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)
        return response.content 

    def load_json(self):
        return json.loads(self.get_response_body()) 
    
requester = GetRequester()
json_data = requester.load_json()
print(json_data)
        
