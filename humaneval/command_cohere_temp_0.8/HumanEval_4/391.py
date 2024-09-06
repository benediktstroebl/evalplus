Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a Markdown code block with corresponding test data and expected output formatting:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

        numbers = [1., 2., 3., 4., 5.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

        numbers = [0., 1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

        numbers = [1., 1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)

        numbers = [0., 0., 1., 2., 3.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

        numbers = [10., 9., 8., 7., 6.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)
```

This script includes a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. 

The function uses the `numpy` library to perform the mean calculation, and the `List` type is used for the input parameter to allow for a variety of tests to be conducted. 

The tests provided evaluate the function's performance across multiple inputs and validate its output against expected values.

Let me know if you would like me to make any modifications to the code or explain anything in more detail.