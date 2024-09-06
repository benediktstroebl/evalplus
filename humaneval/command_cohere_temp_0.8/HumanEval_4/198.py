Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    :return: Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(math.fabs(x - mean) for x in numbers) / len(numbers)
    return mad
```
This script defines a function called `mean_absolute_deviation()` that takes in a list of numbers and calculates the mean absolute deviation of the numbers in the list. 

Here's a breakdown of the code:
1. It imports the `List` module from the `typing` package — this is used for type-checking in the function definition and it imports the `math` module for handy mathematical functions.
2. The `mean_absolute_deviation()` function takes a list of numbers (`List[float])` as an argument, it calculates the mean of the numbers and the absolute deviation from the mean for each number, and then returns the average of these absolute deviations as the mean absolute deviation. 

This should provide you with the calculated Mean Absolute Deviation. 

You can use this function to calculate the Mean Absolute Deviation of a list of numbers by passing the list as an argument, such as `result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])`, and it will return the MAD. 

This approach uses a list comprehension and the `math.fabs()` function to compute the absolute deviation from the mean for each number, and then calculates the average to provide the Mean Absolute Deviation, which is the desired output.