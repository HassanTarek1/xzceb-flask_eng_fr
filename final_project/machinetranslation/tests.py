import unittest
from translator import french_to_english, english_to_french

class TestEnglishToFrensh(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(' '),' ')

class TestFrenshToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(' '),' ')


unittest.main()