import unittest
from python import *
class TestChecking(unittest.TestCase):

    def test_Checking(self):
        self.assertEqual(checking(), 55, "Should be 55")

if __name__ == '__main__':
    unittest.main()
