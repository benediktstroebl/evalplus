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

if __name__ == '__main__':
    unittest.main()
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It converts the input list to a numpy array, calculates the mean of the array, and then calculates the absolute difference between each element of the array and the mean. Finally, it returns the average of these absolute differences.

The script also includes a unit test class `TestMeanAbsoluteDeviation` that checks whether the function behaves as expected on a simple list of numbers. 

You can run this script to see if the function behaves as expected. The `unittest` module is used for unit testing, and `numpy` is used for numerical computations.