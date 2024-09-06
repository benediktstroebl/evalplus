```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset."""
    return float(sum(map(lambda x: abs(x - float(numbers[len(numbers)))), numbers))) / len(numbers)
```

This Python code defines a function called mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation of the dataset.

The function uses the sum function and a lambda function to calculate the sum of the absolute differences between each element in the input list and the mean of the numbers.

The function then divides the sum of absolute differences by the length of the input list to get the Mean Absolute Deviation.