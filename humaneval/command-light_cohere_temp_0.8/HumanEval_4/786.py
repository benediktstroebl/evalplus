```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]):
    # Calculate Mean Absolute Deviation
    mad = math.mean(numbers)
    mad = sum((x - mad) ** 2 for x in numbers) / len(numbers)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print("Mean Absolute Deviation:", mean_absolute_deviation(numbers))

This Python code defines a function called `mean_absolute_deviation` that calculates and returns the Mean Absolute Deviation (MAD) of a list of input numbers.  The function uses the mathematical mean (`math.mean`) to calculate the average of the input numbers and then computes the MAD by summing the squared differences between each element and the mean, divided by the number of elements.

The function is then tested with a list of numbers `[1.0, 2.0, 3.0, 4.0] and the test the expected to print "Mean Absolute Deviation: 4.0".