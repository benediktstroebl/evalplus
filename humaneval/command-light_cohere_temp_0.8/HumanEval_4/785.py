```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    """ Calculates the mean of a list of numbers """
    return sum(numbers)/len(numbers)

def test_mean_absolute_deviation(test_numbers):
    """ Tests the function mean_absolute_deviation against a given list of numbers """
    assert mean_absolute_deviation(test_numbers) == sum(test_numbers)/len(test_numbers)

test_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print out the test_mean_absolute_deviation(test_numbers)

The code defines a function that computes the Mean Absolute Deviation (MAD) of a given list of numbers. The MAD is calculated using the average of the numbers and the absolute difference between each element and the mean.

The function also has a nested helper function that calculates the mean of a list of numbers. The test function tests the function against a sample list of numbers and passes the test.