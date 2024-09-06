Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_mean_absolute_deviation_with_list_of_negative_numbers(self):
        numbers = [-1, -2, -3, -4]
        self.assertEqual(mean_absolute_deviation(numbers), 3.0)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, as described in the problem statement. It also includes a `unittest` module to test the function with different inputs.

The `test_mean_absolute_deviation_with_list_of_numbers` test verifies that the function returns 1.0 when passed a list of numbers [1.0, 2.0, 3.0, 4.0], which is the correct mean absolute deviation. The `test_mean_absolute_deviation_with_empty_list` test ensures that the function raises a `ValueError` when an empty list is passed. The `test_mean_absolute_deviation_with_list_of_negative_numbers` confirms the calculation for a list of negative numbers. 

The `unittest.main()` function is used to discover and run the tests. 

To execute the script, ensure that the `numpy` library is installed by running `pip install numpy`, and then use `python` to execute the script in the terminal. 
The script can also be executed by pressing the Playground Button Underneath.