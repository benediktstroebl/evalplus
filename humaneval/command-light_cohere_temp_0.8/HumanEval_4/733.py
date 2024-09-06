Here's the self-contained Python function that solves the problem:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Declare variables
    mean = sum(numbers) / len(numbers)
    x_mean = mean
    mad = sum((x - x_mean) ** 2 for x in numbers) / len(numbers)
    return mad
```
The provided code defines a function called mean_absolute_deviation, which takes a list of numbers as input and calculates the Mean Absolute Deviation around the mean of the dataset. The MAD is calculated by taking the average of the squared differences between each element in the list and the mean.