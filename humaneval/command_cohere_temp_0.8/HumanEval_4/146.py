Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script utilizes the `numpy` library to provide a more efficient solution. The `mean_absolute_deviation` function takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. It first converts the input list into a numpy array, then calculates the mean of the elements and subtracts it from each number in the array to get the deviation. Then, it calculates the absolute value of each deviation and calculates the mean to return the final result.

The example usage demonstrates how to call the function with a sample list of numbers and prints the result.