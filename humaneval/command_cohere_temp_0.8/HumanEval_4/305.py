Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the absolute deviations from the mean for each number in the input list, and then returns the average of these absolute deviations using the `numpy` library.

You can install the `numpy` library like this:
```bash
pip install numpy
``` 

To test this function, you can use the following code:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 3.0)
        self.assertEqual(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0)

if __name__ == '__main__':
    unittest.main()
```

This test suite includes three test cases to cover different scenarios, ensuring that the function `mean_absolute_deviation` produces the expected outputs for these specific inputs.