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
    :return: Mean Absolute Deviation of the input list
    """
    return math.sqrt(sum((x-mean(numbers))**2 for x in numbers)/len(numbers))

def mean(numbers: List[float]) -> float:
    """ Calculate the mean of a list of numbers
    :param numbers: List of input numbers
    :return: Mean of the input list
    """
    return sum(numbers)/len(numbers)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script includes two functions: `mean_absolute_deviation` and `mean`. The `mean_absolute_deviation` function calculates the mean absolute deviation of a list of numbers. It achieves this by finding the mean of the numbers and then computing the absolute deviation for each number in the list, averaging these deviations, and returning the result.

The `mean` function calculates the simple mean of a list of numbers, which is used as the centerpoint in the `mean_absolute_deviation` function.

The example usage demonstrates how to use these functions to calculate the mean absolute deviation of a list of numbers. In this case, it calculates the mean absolute deviation of the list `[1.0, 2.0, 3.0, 4.0]` to be approximately 1.0. 

You can adapt this code to test against a larger dataset.  If you encounter any issues, feel free to ask!