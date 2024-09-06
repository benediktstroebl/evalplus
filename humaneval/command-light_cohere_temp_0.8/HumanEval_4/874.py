Here's the solution of the problem:
```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculating Mean Absolute Deviation
    mean = sum(numbers)/len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(mad / mean)
```
This script defines a function mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation of the dataset. The MAD is calculated as the average of the squared differences between each element and the mean, and the average of these values is divided by the total number of elements in the dataset.