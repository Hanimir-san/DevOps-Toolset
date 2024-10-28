import os
import unittest

class TestOs(unittest.TestCase):
    """
    Sample test to run with pre-commit hooks
    """

    def test_correct_os(self):
        self.assertEqual(os.sep, '/', msg="How dare you try to run this on Windows you FILTH!")

if __name__ == "__main__":
    unittest.main()