Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test data and expected output, which should pass when executed against the previously defined function:
```python
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        numbers = [-1., 0., 1., 2.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.6666666666666666)
```