URL = "https://api.npoint.io/c790b4d5cab58020d391"

import requests
class Post:
   def get_data(self):
       response = requests.get(url=URL)
       data = response.json()
       return data

