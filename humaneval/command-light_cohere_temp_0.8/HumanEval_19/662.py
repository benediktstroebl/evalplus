```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    # convert string to list of numbers
    numbers_list = list(map(int, numbers. Run tests.
    # verify that input string can convert to list of numbers
    assert isinstance(numbers_list, List), "Input should be a list of numbers")
    # verify the range of numbers
    assert len(numbers_list) > 0, "Input list should not be empty"
    # verify the valid choices
    assert sorted(numbers_list) == ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], \
        "Invalid choice, should be 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', or 'nine'"
    return ' '.join(numbers_list)

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual("three one five")
        assert sort_numbers("three one five") == "one three five"

if __name__ == '__main__':
    unittest.suite.main()


```