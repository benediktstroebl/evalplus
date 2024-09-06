Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(abs(x - mean) for x in numbers) / len(numbers)
    return math.sqrt(dev)
```

This function calculates the mean of the input list of numbers and then finds the absolute deviation of each number from the mean. It then calculates the average of these absolute deviations and returns the square root of this value, which is the Mean Absolute Deviation. It assumes the provided 'numbers' list contains at least one numerical value.

You can use this function by passing a list of numbers as an argument, and it will return the mean absolute deviation for those numbers. You can also modify the function to handle cases where the input list is empty or contains non-numeric values by adding appropriate exception handling.