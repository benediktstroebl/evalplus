Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a Markdown code block with corresponding tests:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        numbers = [-1., 0., 1., 2.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.666_666)

    def test_mean_absolute_deviation_with_single_value(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)
```

This way, the code will first define a test class with different test scenarios and then run the test class against the function, outputting the test results in the Markdown code block.