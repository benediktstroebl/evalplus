```python
from typing import List
import numpy as np
import unittest

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list to find the minimum and maximum values
    numbers = np.sort(numbers)
    
    # Apply a linear transform to the list
    rescaled_numbers = (numbers - numbers[0]) / (numbers[-1] - numbers[0])
    
    # Return the rescaled list as a Python list
    return rescaled_numbers.tolist()

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]), [1.0, 0.75, 0.5, 0.25, 0.0])

    def test_rescale_to_unit_edge_cases(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([1.0])
        with self.assertRaises(ValueError):
            rescale_to_unit([])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `rescale_to_unit` function as specified in the problem, along with a unit test class to verify its correctness. It uses the NumPy library for sorting the input list and performing the linear transform. The unit test class includes test cases for the specified example, as well as edge cases (lists with less than two elements).