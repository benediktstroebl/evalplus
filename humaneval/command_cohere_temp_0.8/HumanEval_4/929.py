Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module 1: function and documentation
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    mean_value = sum(numbers) / len(numbers)     # calc the mean value
    mad = sum(abs(x - mean_value) for x in numbers) / len(numbers)  # calc MAD
    return mad

# module 2: tests
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
        self.assertEqual(mean_absolute_deviation([0., 0., 0.]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([-1., -2., -3., -4.]), 3.0, places=1)

if __name__ == '__main__':
    unittest.main()
```

When you run the script, the `unittest` framework will execute the test cases and report on whether the function's outputs match the expected values. This separation of concerns into function and tests is a key aspect of writing maintainable code.