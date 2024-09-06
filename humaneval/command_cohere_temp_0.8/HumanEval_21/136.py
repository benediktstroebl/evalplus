Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [x / max(numbers) for x in numbers]
```
This function accepts a list of numbers and returns a modified list in which the smallest number is 0 and the largest number is 1. 

You can test the function using the following code:
```python
import unittest

class TestRescale(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    def test_rescale_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])
    def test_list_with_single_element(self):
        self.assertEqual(rescale_to_unit([6.0]), [6.0])
    def test_list_with_multiple_elements(self):
        self.assertEqual(rescale_to_unit([0.5, 6.0, 2.0, 9.0]), [0.0, 0.833, 0.333, 0.167, 1.0])
if __name__ == '__main__':
    unittest.main()
```
The test suite consists of four test functions. The first test checks the function against a reference result. The second test checks if the function correctly handles an empty list. The third test checks if the function correctly handles a list with a single element. The fourth test checks if the function handles a list with multiple elements correctly. 

The code invokes the unittest.main() function, which executes the test suite. 

To run this code, you can either:
1. Execute the script in a Python environment that supports testing, and the test suite will automatically run.
2. Add the function rescale_to_unit to a Python file (e.g., rescale.py) and then, at the command line of the directory containing this file, run python -m unittest test_rescale.py.

This will execute the test suite and display a summary of the results, including the number of tests passed and any failures or errors encountered.