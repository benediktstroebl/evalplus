```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and rescales the numbers so that the smallest number in the list becomes 0 and the largest number becomes 1. The function first finds the minimum and maximum values in the list using the `min` and `max` functions, respectively. It then calculates the rescaled value of each number in the list by subtracting the minimum value, dividing by the difference between the maximum and minimum values, and returning the adjusted value for each number. 
Here is a simple test case using `unittest` to validate the functionality of the function:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # As stated in the original problem, expected output is [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
```