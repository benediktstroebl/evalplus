Here's the self-contained Python function:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the dataset.
    """
    numbers = sorted(numbers)  # sort the list to ensure the mean is at the center of the data
    mean = sum(numbers)/len(numbers)
    mad = sum((x-mean)**2 for x in numbers) / len(numbers)
    return mad
```
The function takes a list of numbers and calculates the Mean Absolute Deviation, which is the average absolute difference between each element and the mean of the dataset.

This function is self-contained, which means it can be used directly without the need for any external functions or classes. It is a a pure and efficient way to solve the problem in a standalone manner.