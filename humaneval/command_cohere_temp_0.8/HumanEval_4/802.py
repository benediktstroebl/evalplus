Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test code:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        numbers = [-1., 0., 1., 2.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.6666666666666666)

if __name__ == '__main__':
    unittest.main()
```

This script and test code demonstrate how to use the `mean_absolute_deviation` function to calculate the mean absolute deviation of a list of numbers and how to validate this function with test cases. 

This Python script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. This function leverages the `numpy` library to operate on arrays and perform mathematical operations efficiently. The test cases included cover scenarios such as a list of positive numbers and a list containing negative values, ensuring that the function produces correct results across different scenarios.