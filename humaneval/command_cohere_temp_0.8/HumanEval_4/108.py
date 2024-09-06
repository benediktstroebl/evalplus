Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the list
    """
    mean = math.mean(numbers)
    deviation = sum(math.abs(num - mean) for num in numbers) / len(numbers)
    return deviation
```
This script includes a function called `mean_absolute_deviation()` that calculates the mean absolute deviation of a list of numbers. The function takes a list of numbers as input and returns the mean absolute deviation of the list. 

It calculates the mean of the list `mean = math.mean(numbers)` and then calculates the absolute deviation for each number in the list: `deviation = sum(math.abs(num - mean) for num in numbers) / len(numbers)`. 

The script returns the mean absolute deviation of the list. 

To ensure that the function is correct, it is possible to test it using Python's `unittest` module:
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_single_number(self):
        """Test case for a list containing a single number"""
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_mean_absolute_deviation_two_numbers(self):
        """Test case for a list containing two numbers"""
        self.assertEqual(mean_absolute_deviation([1.0, 2.0]), 1.0)

    def test_mean_absolute_deviation_three_numbers(self):
        """Test case for a list containing three numbers"""
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)

    def test_mean_absolute_deviation_four_numbers(self):
        """Test case for a list containing four numbers"""
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0) 

if __name__ == '__main__':
    unittest.main()
```
In this example, we use Python's `unittest` module to create four test cases that validate the behaviour of the `mean_absolute_deviation` function for lists of different lengths. The `unittest.main()` function executes the tests when the script is run directly. 

These tests check that the function behaves as expected, but you can add more tests to cover a broader range of scenarios according to your needs.  If you install `pytest` you can also use the [pytest testing framework](<https://docs.pytest.org/en/latest/>) which is more modern and often preferred.  You can use `python -m pytest test_mean_absolute_deviation.py` to execute your tests.  It will automatically discover the tests in your file.  You can also use the `unittest` framework with `python test_mean_absolute_deviation.py` but you would need to explicitly declare what tests you want like we did with the `unittest.suite()` function