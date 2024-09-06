Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This transformation is a linear transformation.

To test this function, you can run the following code:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    def test_rescale_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])
    def test_rescale_single_number(self):
        self.assertEqual(rescale_to_unit([6.0]), [0.0])
    def test_rescale_multiple_numbers(self):
        self.assertEqual(rescale_to_unit([2.0, 5.0, 8.0, 1.0, 4.0]), [0.25, 0.75, 1.0, 0.0, 0.5])
if __name__ == '__main__':
    unittest.main()
```

This test suite includes several test functions to validate the behavior of the `rescale_to_unit` function for different scenarios. Specifically, it checks for the following scenarios: 
- The test `test_rescale_to_unit` ensures that the function correctly rescales a list of numbers.
- The test `test_rescale_empty_list` ensures that the function handles an empty list correctly by returning an empty list.
- The test `test_rescale_single_number` checks if the function correctly handles a list with a single element.
- The test `test_rescale_multiple_numbers` verifies the function's ability to correctly rescale a list of numbers. 

When you run this code, Python's built-in testing tool unittest will execute each test case, and the output will indicate whether the tests pass or fail.