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
    if len(numbers) == 0:
        return 0.0  # handle empty list

    # calculating mean of the list
    mean = sum(numbers) / len(numbers)

    # calculating absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    return math.fsum(absolute_deviations) / len(numbers)
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of floats as input and returns the mean absolute deviation as a float. 

The mean absolute deviation is calculated by first computing the mean of the list. Then, the code calculates the absolute deviation of each number in the list from the mean, and these absolute deviations are summed up and divided by the number of elements in the list.

To ensure robustness, the script includes a test for an empty list, returning 0 in such a case.

You can use this function to calculate the mean absolute deviation of any list of numbers by calling it and passing the list as an argument, as demonstrated in the docstring example.