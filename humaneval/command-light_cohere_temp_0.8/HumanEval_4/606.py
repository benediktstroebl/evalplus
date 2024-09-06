```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) ->
    # The absolute value of the difference between each element and the mean of the dataset
    mad = 0.0
    for n in numbers:
        mad += math.abs(n - numbers[-1] )
    mad = mad / len(numbers)
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```
This code defines a Python function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. It does this by calculating the absolute value of the difference between each element and the mean of the dataset, then taking the average of these absolute differences.