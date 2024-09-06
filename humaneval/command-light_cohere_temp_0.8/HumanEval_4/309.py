```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Center of Gravity is mean of the list.
    mean = sum(numbers) / len(numbers)
    mad = 0.0
    for num in numbers:
        mad = mad + math.abs(num - mean)
    mad = mad / len(numbers)
    return mad

# Test case for function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 0.0)
```
This code defines a function `mean_absolute_deviation` that takes a list of numbers and returns the Mean Absolute Deviation (MAD) as a float. The function first calculates the mean of the list, then uses this mean to calculate the MAD by summing the absolute differences of each element from the mean and dividing by the total number of elements.