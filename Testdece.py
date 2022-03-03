import json
import requests
import unittest
from urllib.request import urlopen
#from bs4 import BeautifulSoup

class FlaskTestCase(unittest.TestCase):
    URL1 = "http://127.0.0.1:5000/getall"
    URL2 = "http://127.0.0.1:5000/postdata"
    URL3 = "http://127.0.0.1:5000/deletedata"
    URL4 = "http://127.0.0.1:5000/updatedata"
    #data for the post method
    dataTest = {
        "index" : 5,
        "Decepticon" : "Soundblaster",
    }
    #data for the update method   
    updated_data = {
        "index" : 73,
        "Decepticon" : "Knock Out",
    }
    

    def test_getall_data(self):
        response = requests.get(self.URL1)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(response.json()), 1)
        print("test 1 completed")
    
    def test2_post_data(self):
        response = requests.post(self.URL2, json=self.dataTest)
        self.assertEqual(response.status_code, 200)
        print("test 2 completed")

    #test qui permet de vérifier si l'on peut trouver un data spécifique
    def test_get_specific_data(self):
        response = requests.get(self.URL1 + '/Swindle')
        self.assertEqual(response.status_code, 200)
        print("test 3 is completed") 
    #test qui permet de vérifier si l'api peut delete une data

    def test_delete_data(self):
        response = requests.delete(self.URL3 + '/Dirge')
        self.assertEqual(response.status_code, 200)
        print("test 4 completed") 

    #test qui permet de vérifier si l'on peut modifier une donnée
    def test_update_data(self):
        response = requests.put(self.URL4 + '/Frenzy', json=self.updated_data)
        print(response.json())

        self.assertEqual(response.json()['Decepticon'], self.updated_data['Decepticon'])
        print("test 5 completed")
#condition pour dire que le server est lancé
if __name__ == "__main__":
    unittest.main()