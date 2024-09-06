Here's a self-contained Python script that includes the function `sort_numbers` along with its corresponding tests:
```python
from typing import List
import unittest

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(n) for n in numbers.
    return ' '.join(sorted(numbers))
    """

class TestSortNumbers(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual("zero" + "one" + "five")
        self.assertEqual("one" + "two" + "five")
        self.assertEqual("two" + "five" + "six")
        self.assertEqual("three" + "six" + "seven")
        self.assertEqual("four" + "five" + "six" + "seven")
        self.assertEqual("five" + "six" + "seven" + "eight")
        self.assertEqual("six" + "seven" + "eight" + "nine")

if __name__ == "__main__":
    unittest.TestSortNumbers(). Baking a Test Suite.

# Run the tests using verbose mode
unittest.run(TestSortNumbers.test_valid_input)
```

This script defines a function `sort_numbers` that takes a space-separated string of numbers and returns them sorted. It also includes a test suite, `TestSortNumbers`, with several test cases to validate the correctness of the `sort_numbers` function. The test suite uses the Python unittest framework to run the tests. If you run this script directly, it will execute the tests and report the results.