Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(math.fabs(x - mean) for x in numbers) / len(numbers)
    return mad
```

And here is a corresponding test case:
```python
def test_mad_calculation():
    """ Tests the mean_absolute_deviation function """
    numbers = [1., 2., 3., 4.]
    expected = 1.0
    result = mean_absolute_deviation(numbers)
    assert result == expected
```

This script defines a function `mean_absolute_deviation()` that calculates the mean absolute deviation of a list of numbers. 

The `test_mad_calculation()` function tests the `mean_absolute_deviation()` function with a sample numeric dataset [1., 2., 3., 4.]; these are dummy numerical data points that are easy to work with for a test. The test is created to check if the Mean Absolute Deviation calculated by the function is equal to the expected result, which in this case is 1.0. 

To run the test, you would use the `pytest` library, which is commonly installed via `pip install pytest`, and then run `pytest test_file.py` from the command line, where `test_file.py` is the file that contains the test code. 

This script demonstrates the use of numerical statistical methods in Python, leveraging Python's typing, list comprehension, and mathematical libraries to calculate MAD, a measure of the variability of a dataset. 

Depending on your use case, you may wish to explore other statistical measures such as the standard deviation as alternatives or additional comparisons.