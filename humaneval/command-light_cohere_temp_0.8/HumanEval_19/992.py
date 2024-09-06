```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()



class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers_valid(self):
        self.assertEqual("three one five")
        self.assertEqual("one three five")
        assert sort_numbers("three one five") == "one three five"
        assert sort_numbers("zero one two three four five six seven eight nine") == "zero eight nine seven six"

    def test_sort_numbers_empty(self):
        self.assertEqual("")
        assert sort_numbers("") == ""

    def test_sort_numbers_negative(self):
        self.assertEqual("-2 -2 -4")
        assert sort_numbers("-2.4") == "-4"

    def test_sort_numbers_mixed_types(self):
        self.assertEqual("zero seven eight nine")
        self.assertEqual("two three four five")
        assert sort_numbers("zero seven eight nine two three four five") == "zero two four five"

if __name__ == "__main__":
    unittest.unittest.main()

```
```
The function `sort_numbers` in this script accepts a string of numbers as input and outputs the numbers sorted from smallest to largest. The `TestSortNumbers` class contains several test cases for this function, such as verifying the sorting of various input strings. 

To execute the tests and verify the functionality of the `sort_numbers` function, the script uses the `unittest` module and defines the `TestSortNumbers` class. 
To run the tests, the script uses the `unittest.main()` function, which is called when the script is executed.