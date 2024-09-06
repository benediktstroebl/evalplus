Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    # Initialize variables
    x_mean = sum(numbers) / len(numbers)
    mad = 0.0
    for x in numbers:
        # Calculate the difference from the mean
        x_dev = x - x_mean
        # Calculate the absolute value of the difference
        x_abs = math.abs(x_dev)
        # Add the difference to the Mean Absolute Deviation
        mad += x_abs
    # Return the Mean Absolute Deviation
    return mad
# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
```
This function takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) for that list. The MAD is calculated by finding the average of the absolute differences between each element and the mean of the dataset.

It adds up the absolute differences to the running sum of the Mean Absolute Deviation, which is then returned.