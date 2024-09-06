```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """ MAD = sum((x - x_mean) ** 2) / len(numbers)
    return MAD

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print("Calculated Mean Absolute Deviation:", mean_absolute_deviation(numbers))

``` 
This code defines a Python function called mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation. The MAD is calculated using the formula MAD = sum((x - x_mean) ** 2) / len(numbers), where MAD is the mean of the absolute deviations of each element from the mean, x_mean is the mean of the input list, and x is each element in the input list. 
This function is then tested by passing a sample list of numbers and printing the result.