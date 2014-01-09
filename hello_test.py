__author__ = 'jinfeng'

import unittest
import hello

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, hello.add(2, 3))

    def test_add2(self):
        self.assertEqual(30, hello.add(10, 20))

if __name__ == '__main__':
    unittest.main()