Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module code
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    dev = sum(abs(x - mean) for x in numbers) / len(numbers)
    return dev

# test code
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0) 
    def test_mean_absolute_deviation_with_larger_dataset(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), 2.5) 

if __name__ == '__main__':
    unittest.main()
```

In this script, the `mean_absolute_deviation` function calculates the Mean Absolute Deviation of a list of numbers. It is tested twice - first for a smaller dataset (`[1.0, 2.0, 3.0, 4.0]`), and then for a larger one (`[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]`). The tests are executed when the script is run directly (using `unittest.main()`). 

This way, you have a self-contained Python module with a function to calculate the Mean Absolute Deviation and a set of tests to validate its correctness.  If you wish to use this function in other parts of your project, you can import it as `import mean_absolute_deviation from 'path_to_this_script.py'`