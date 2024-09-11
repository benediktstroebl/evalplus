**Rescaling a List of Numbers to Unit Range**
=============================================

Here's a Python script that includes the `rescale_to_unit` function, along with a simple test case to demonstrate its usage:
```python
from typing import List
import unittest

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

if __name__ == "__main__":
    unittest.main(argv=[None, '-v'])
```
This script uses the `min` and `max` functions to find the smallest and largest numbers in the input list, and then applies a linear transformation to each number to rescale it to the unit range `[0.0, 1.0]`. The `unittest` framework is used to test the `rescale_to_unit` function with a simple test case.