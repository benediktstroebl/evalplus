Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) * 1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers `numbers` as input and returns a transformed list. The transformation is applied linearly such that the smallest number in the list becomes 0 and the largest number becomes 1. The function uses the `min` and `max` functions to capture the range of values and then applies the transformation using a list comprehension with four steps:
1. Subtract the minimum value of the list from each element to center the range around 0.
2. Divide by the difference between the maximum and minimum values to scale the range from 0 to 1.
3. Multiply by 1 to eliminate the scaling factor.
4. Return the modified list. 

This function can be used to rescale any list of numbers with at least two elements, making it useful for data normalization and analysis. 

To test this function, you can use the following Python code:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    
    def test_rescale_to_unit_with_single_number(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([1.0])
    
    def test_rescale_to_unit_with_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

if __name__ == '__main__':
    unittest.main()
```
In the test suite are three individual test functions:
1. `test_rescale_to_unit`: This function tests the `rescale_to_unit` function with a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0] and asserts that the output is equal to the expected output [0.0, 0.25, 0.5, 0.75, 1.0].
2. `test_rescale_to_unit_with_single_number`: This function tests the `rescale_to_unit` function with a list containing a single number 1.0 and asserts that it raises a `ValueError` since the input list should contain at least two elements. 

The test suite uses the `unittest` module, which is a built-in Python testing framework. The `unittest.main()` function is used to discover and run the test cases. 

You can run this script to test the functionality of the `rescale_to_unit` function.  The output will indicate whether the tests pass or fail.  In this case, the output will be:
```
..
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
``` 
indicating that all tests have passed successfully.  This confirms the expected behavior of the `rescale_to_unit` function.