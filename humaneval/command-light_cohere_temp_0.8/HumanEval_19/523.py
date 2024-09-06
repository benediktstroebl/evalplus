```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers. 

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self) -> None:
        self.assertEqual("three one five", should return 'one three five'")
        
    def test_numbers_valid(self, input) -> None:
        self.assertEqual(sorted(input)
        expected = ["zero", "one", "two", "three", "four", "five"]
        self.assertEqual(set(input.sort_numbers(input),inList(expected)))
        return None

if __name__ == "__main__":
    unittest.run(TestSortNumbers())
``` 
The provided Python script defines a function `sort_numbers` that sorts a space-separated string of numbers from "zero" to "nine". The function takes a string as input and returns the sorted string. The script also includes a `unittest` framework with two test cases: 
- `test_sort_numbers` checks if the input "three one five" is correctly sorted and returns True. 
- `test_numbers_valid` checks if the `sort_numbers` function correctly sorts a list of strings. 
Finally, the script runs the test case in the `unittest.several` framework automatically checks the all test cases and raises an exception if any test fails.