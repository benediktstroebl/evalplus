Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    return rescaled_numbers
```

To ensure that the `rescale_to_unit` function works correctly, we can write a few test cases that cover various scenarios. Here's how you could structure some test cases using Python's `unittest` framework:
```python
import unittest
from rescale_to_unit import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(rescale_to_unit([1.0]), [0.0])

    def test_small_range(self):
        self.assertEqual(rescale_to_unit([0.5, 1.0, 1.5]), [0.0, 0.5, 1.0])

    def test_large_range(self):
        self.assertEqual(rescale_to_unit([0.1, 1.0, 2.0, 3.0, 4.0]), [0.0, 0.333, 0.667, 1.0, 1.333])

    def test_already_normalized(self):
        self.assertEqual(rescale_to_unit([0.1, 0.2, 0.3]), [0.1, 0.2, 0.3])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

    def test_list_with_single_element(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([1.0, 1.0, 1.0])

if __name__ == '__main__':
    unittest.main()
```

In this test suite, we cover the following scenarios:
- Test `test_single_number`: Validates that the function correctly handles a list with a single element.
- Test `test_small_range`: Checks if the function correctly handles a list with a small range of values.
- Test `test_large_range`: Asserts that the function handles a list with a larger range of values.
- Test `test_already_normalized`: Verifies that the function correctly handles a list that is already normalized.
- Test `test_empty_list`: Checks if the function raises a `ValueError` when an empty list is passed.
- Test `test_list_with_single_element`: Validates that the function raises a `ValueError` when a list with a single element is passed.

To run these tests, you can use the `unittest` module, by executing the script or calling `python test_rescale_to_unit.py` and the test results will be displayed at the end. 

By executing these tests, you can confirm that the `rescale_to_unit` function behaves as expected across various scenarios, providing reliable assurance of its functionality.