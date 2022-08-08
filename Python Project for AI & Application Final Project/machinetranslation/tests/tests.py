
import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), None) # 
    def test2(self):
        self.assertEqual(englishToFrench("Hello")['translations'][0]['translation'], 'Bonjour')  # 

class TestFrToEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), None) # 
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour")['translations'][0]['translation'], 'Hello')  # 
unittest.main()
