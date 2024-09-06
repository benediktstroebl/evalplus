Here is a self-contained Python script that solves the problem you've outlined:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset."""
    mean = sum(numbers)/len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
```
This Python code defines a function mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation as a float. The MAD (mean absolute deviation) is the average absolute difference between each element in the list and the mean.