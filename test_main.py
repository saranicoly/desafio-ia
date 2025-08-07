import unittest
from unittest.mock import patch
from io import StringIO
from main import is_bulky, is_heavy, sort, main

class TestMain(unittest.TestCase):
    def test_is_bulky(self):
        self.assertTrue(is_bulky(150, 50, 50))  # Bulky by width
        self.assertTrue(is_bulky(50, 150, 50))  # Bulky by height
        self.assertTrue(is_bulky(50, 50, 150))  # Bulky by length
        self.assertTrue(is_bulky(100, 100, 100))  # Bulky by volume
        self.assertFalse(is_bulky(10, 10, 10))   # Not bulky

    def test_is_heavy(self):
        self.assertTrue(is_heavy(20))   # Heavy
        self.assertFalse(is_heavy(19.99))  # Not heavy

    def test_sort(self):
        self.assertEqual(sort(150, 50, 50, 25), "REJECTED")  # Bulky and heavy
        self.assertEqual(sort(150, 50, 50, 15), "SPECIAL")   # Bulky but not heavy
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")    # Not bulky but heavy
        self.assertEqual(sort(50, 50, 50, 15), "STANDARD")   # Neither bulky nor heavy
        
    @patch('builtins.input', side_effect=["a", "50", "50", "10"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_handling(self, mock_stdout, mock_input):
        result = main()

        self.assertRaises(ValueError)
        self.assertIsNone(result)
