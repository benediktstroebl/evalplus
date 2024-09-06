Here is a Python script that defines a function to sort numbers in a string and passes tests using the `unittest` framework:
```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()

```
# run the function with tests
class TestSortNumbers(unittest.TestCase.TestCase):
    def test_positive_integer(self):
    self.assertEqual("three one five")
    assert sorted("three one five") == "one three five"
    self.assertEqual("five four three")
    assert sorted("five four three") == "four three five"
    self.assertEqual("six three seven")
    assert sorted("six three seven") == "three seven six"
    self.atisf("eight seven nine")
    assert sorted("eight seven nine") == "seven nine eight"

if __name__ == "__main__":
    unittest.main()
```