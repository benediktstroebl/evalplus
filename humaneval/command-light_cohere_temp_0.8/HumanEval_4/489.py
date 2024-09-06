Here is a Python script that contains a self-contained function with a docstring that solves the given problem:

```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. The average absolute difference between each
    element and the mean of the dataset.
    # Find the mean
    x_mean = sum(numbers) / len(numbers)
    # Calculating the absolute deviation
    abs_deviation = sum((x - x_mean) for x in numbers) / len(numbers)
    # Returning the MAD value
    return math.sqrt(abs_deviation)
```
This script defines a function called `mean_absolute_deviation` that takes a list of numbers as an argument and returns the Mean Absolute Deviation of the list.

The `abs_deviation` variable is a sum of the differences between each element in the `numbers` list and the mean of the list, divided by the length of the list.

The `mad` variable is the square root of the `abs_deviation` variable.