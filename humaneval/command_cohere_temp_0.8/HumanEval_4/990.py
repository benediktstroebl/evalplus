Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_ EmptyList(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])
    def test_ListWithOneItem(self):
        self.assertEqual(mean_absolute_deviation([1.]), 0.0)
    def test_LargeList(self):
        numbers = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
        result = mean_absolute_deviation(numbers)
        expected = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
``` 

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` module to operate on the input list and calculate the deviation. 

The script also includes a set of unit tests for the function using the `unittest` module. The tests cover scenarios such as an empty list, a list with one item, and a large list of numbers. 

The `TestMeanAbsoluteDeviation` class defines the test methods, and `unittest.main()` executes the tests when the script is run directly. 

Please note you'll need to have the Numpy library installed to use the provided code:
```bash
pip install numpy
```

This way, you can ensure the functionality of the function and verify that it complies with the problem statement.