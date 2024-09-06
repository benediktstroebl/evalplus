Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to demonstrate its use:
```python
# -*- coding: utf-8 -*-
import numpy as np
import unittest

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).

    Parameters:
        numbers (list of float): List of numerical data.

    Returns:
        float: Mean Absolute Deviation value.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        """
        Test case for mean_absolute_deviation function.
        """
        numbers = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to provide an efficient implementation. 

The `TestMeanAbsoluteDeviation` class runs a test case where we call the `mean_absolute_deviation` function with a list of numbers, and it checks that the result is correct. 

To run the test, simply execute the script, and the `unittest` framework will run the test case and provide the result. 

This approach maintains a clear separation between the function and its corresponding test, which is considered a best practice in testing methodologies. 

Let me know if you have any further questions!