Here is a self-contained Python script with a function that solves the problem of sorting a list of numbers in markdown code block:
```python
from typing import List
import unittest

def sort_numbers(numbers: List[int]) -> str:
    """ Input is a list of integers, valid choices are 'zero', 'one', ...
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers([0, 1, 5])
    'zero one five'
    """
    return " ".join(str(x) for x in sorted(numbers))

class TestSortNumbers(unittest.TestCase.TestCase):
    def test_return_string(self):
        self.assertEqual("zero one two five")
        return "one zero five"

if __name__ == "__main__":
    unittest.TestCase.assert()
    different test test()
```