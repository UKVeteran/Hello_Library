# tests/test_module.py

import unittest
from my_library import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
