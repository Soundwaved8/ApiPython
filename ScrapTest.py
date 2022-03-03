import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Test(unittest.TestCase):
    bs = None
    def setUpClass():
        url = 'https://transformers.fandom.com/fr/wiki/Decepticon'
        Test.bs = BeautifulSoup(urlopen(url), 'html.parser')
        print("la page à bien été trouvé")

    def test_exists(self):
        contenu = Test.bs.find('span',{'class':'new'})
        self.assertIsNotNone(contenu)

    def test_Title(self):
        title = Test.bs.find('h1', {'class':'page-header__title'})
        self.assertIsNotNone(title)
        print("test 2 completed")
    
if __name__ == "main":
    unittest.main()