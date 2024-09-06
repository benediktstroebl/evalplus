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
    if len(numbers) == 0:
        return 0.0  # Return 0 dev if an empty list is passed
    mean = math.fmean(numbers)  # Mean of the list
    deviation = sum(math.fabs(x - mean) for x in numbers) / len(numbers)  # Absolute deviation of each number
    return deviation
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of numbers as input and returns the mean absolute deviation of the list. The function first calculates the mean of the list and then the absolute deviation of each number in the list from the mean. The function then returns the average of these absolute deviations.

The `math.fmean` function is used to calculate the mean of the list, and the `math.fabs` function is used to calculate the absolute value of the difference between each number and the mean. The `sum` function is used to sum the absolute deviations, and the `len` function is used to get the length of the list.