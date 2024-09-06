Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. The function does not assume any particular value for the input list, as shown in the test case below. 

This script can be imported and executed independently from another file, and the function can be called directly to process a list of numbers. Here is an example of how you can use this function:
```python
import rescale_to_unit

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit.rescale_to_unit(numbers))
```
This will output:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```
To further ensure that the function behaves as expected, below is a simple test suite that can be executed together with the function definition to verify its behavior:
```python
import unittest
def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]

class TestRescaleToUnit(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(rescale_to_unit([1.0]), [0.0])

    def test_two_numbers(self):
        self.assertEqual(rescale_to_unit([0.5, 1.5]), [0.0, 0.5])

    def test_three_numbers(self):
        self.assertEqual(rescale_to_unit([0.0, 0.5, 1.0]), [0.0, 0.25, 0.5])

    def test_three_numbers_negative(self):
        self.assertEqual(rescale_to_unit([-1.0, 0.0, 1.0]), [0.0, 0.5, 1.0])

    def test_large_numbers(self):
        self.assertEqual(rescale_to_unit([0.01, 100.00, 1.00, 1000.00]), [0.0, 0.1, 0.5, 0.9])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

    def test_list_with_single_element(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([1.0, 1.0, 1.0])

    def test_unique_elements(self):
        self.assertEqual(rescale_to_unit([0.0, 0.5, 1.0, 1.0]), [0.0, 0.25, 0.5, 0.75])

if __name__ == '__main__':
    unittest.main()
```