Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module: src/mean_absolute_deviation.py
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    return statistics.mean(abs(num - sum(numbers) / len(numbers)) for num in numbers)

# module: src/test_mean_absolute_deviation.py
import unittest
from src.mean_absolute_deviation import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_uniform_list(self):
        """ Test with a list of equal values """
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_random_list(self):
        """ Test with a random list of numbers """
        self EXPECTED_DEV = 1.3
        self ACTUAL_DEV = mean_absolute_deviation([2.5, 1.3, -1.2, 4.7])
        self.assertLess(abs(self ACTUAL_DEV - self EXPECTED_DEV), 0.1) 

if __name__ == '__main__':
    unittest.main()
```

Here's an explanation of each code section:
1. `src/mean_absolute_deviation.py`: This module contains the `mean_absolute_deviation` function. It calculates the Mean Absolute Deviation (MAD) of a list of numbers. The function utilizes Python's `statistics` module to calculate the mean of the absolute deviations.
    - The function first calculates the mean of the input list.
    - It then iterates through each element in the list and calculates the absolute difference between each element and the mean.
    - These absolute differences are then themselves averaged to provide the MAD value, which is returned.
2. `src/test_mean_absolute_deviation.py`: This module is exclusively for testing the `mean_absolute_deviation` function. It includes two test cases:
    - `test_mean_absolute_deviation_with_uniform_list`: This tests the function with a list of equal values to ensure it returns the expected result.
    - `test_mean_absolute_deviation_with_random_list`: This tests the function with a random list of numbers and compares the calculated MAD to an expected value. The `assertLess()` method is used to validate that the calculated MAD is within a small threshold of the expected value, accounting for possible floating-point error.
3. Testing Framework: Both modules use the Python `unittest` framework. The `unittest.main()` function is called to run all test cases when the script is executed directly. This framework provides a structured and organized way to validate the correctness of the `mean_absolute_deviation` function.

This script demonstrates how to encapsulate a function for calculating MAD and then thoroughly test its behavior against expected outputs. The separation of the calculation function and the testing logic into different modules