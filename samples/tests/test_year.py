import unittest
import os

from datetime import datetime

class TestDate(unittest.TestCase):
    """
    Sample test to run with pre-commit hooks
    """

    def test_correct_date(self):
        year_current = datetime.now().year
        self.assertGreaterEqual(year_current, 2024, msg="I do not trust you or your time settings.")

if __name__ == "__main__":
    unittest.main()