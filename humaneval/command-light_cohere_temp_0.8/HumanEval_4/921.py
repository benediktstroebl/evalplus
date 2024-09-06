```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    mean 
    numbers = sorted(numbers)
    mean = sum(numbers) / len(numbers)
    x_mean = mean
    mad = 0
    for x in numbers:
        mad += abs(x - mean)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print("The mean absolute deviation is:", mean_absolute_deviation(numbers)) + "\n")
``` 
This script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation of a given list of numbers. The MAD is calculated using a sliding window approach, where the elements of the list are sorted, and then the mean and mean of the dataset are calculated. The function then computes the absolute difference between each element and the mean, and finally returns the Mean Absolute Deviation.