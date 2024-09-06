Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To ensure that the function works correctly, we can write automated tests. In this case, we can use Python's built-in `unittest` module.

You can create a test case in a separate file called `test_rescale_to_unit.py` to verify the functionality of the `rescale_to_unit` function. Here's what such a test file could look like:
```python
import unittest
from rescale_to_unit import rescale_to_unit # assume it's imported from a file called rescale_to_unit.py

class TestRescaleToUnit(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_single_number(self):
        self.assertEqual(rescale_to_unit([6.0]), [6.0])

    def test_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])

    def test_list_with_single_element(self):
        self.assertEqual(rescale_to_unit([0.0]), [0.0])

    def test_large_list(self):
        large_numbers = [i for i in range(10000, 0, -1)]
        large_numbers = rescale_to_unit(large_numbers)
        self.assertEqual(large_numbers[0], 0.0)
        self.assertEqual(large_numbers[-1], 1.0)

if __name__ == '__main__':
    unittest.main()
```
This test file provides five test cases to cover different scenarios. 
- `test_basic`: This is the primary test, applying the function to the list [1.0, 2.0, 3.0, 4.0, 5.0], comparing the result to the expected output.
- `test_single_number`: Validates that the function handles a list with a single element (e.g., [6.0]) and returns the same element.
- `test_empty_list`: Checks that the function handles an empty list correctly.
- `test_list_with_single_element`: This test validates the function's behavior when the input list contains a single element, such as [0.0].
- `test_large_list`: This test uses a list of numbers ranging from 10000 to 0, applying the function and checking that the results are roughly 0.0 and 1.0.

To run the tests, you can use the `unittest` module by executing the following command in your terminal:
```bash
python -m unittest test_rescale_to_unit
```
This command will run the tests and report any failures or errors. 

This testing approach provides an important layer of assurance, helping us validate the behavior of the `rescale_to_unit` function and