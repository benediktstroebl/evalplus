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
    """
    if not numbers:
        raise ValueError("Input list is empty. Unable to calculate MAD.")

    mean = math.fmean(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)

    return mad
```

This script includes the `mean_absolute_deviation` function that takes a list of numbers as input and calculates the mean absolute deviation of the list. The function first checks if the input list is empty and raises a `ValueError` if it is. It then calculates the mean of the numbers using the `math.fmean` function (using the `math` module). It calculates the absolute deviation by iterating over the list and summing the absolute differences between each element and the mean, and then dividing it by the number of elements.

To ensure that the function behaves correctly, we include tests in the same file in the following section:
```python
# Tests for mean_absolute_deviation function
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_empty_input(self):
        self.assertRaises(ValueError, mean_absolute_deviation, [])

    def test_single_value(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_symmetrical_deviation(self):
        numbers = [1., 2., 3., 4.]
        mean = float(sum(numbers)) / len(numbers)
        expected = sum(abs(x - mean) for x in numbers) / len(numbers)
        self.assertEqual(mean_absolute_deviation(numbers), expected)

    def test_large_deviation(self):
        numbers = [1., 1000., 3., 4.]
        mean = float(sum(numbers)) / len(numbers)
        expected = sum(abs(x - mean) for x in numbers) / len(numbers)
        self.assertEqual(mean_absolute_deviation(numbers), expected)

if __name__ == '__main__':
    unittest.main()
```

This script tests the `mean_absolute_deviation` function with various scenarios, including an empty input list, a list with a single value, and lists with symmetrical and large deviations. 

To run the test, you can run the script file as it is, and the `unittest` framework will run the test cases. You can do this by saving the script to a `.py` file and then executing the file in your Python environment of choice. 

This code should address the task you had outlined, and the test suite ensures its correctness. Let me know if you have any questions or if you would like to troubleshoot any potential issues!