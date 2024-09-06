Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation (MAD) of a given list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Mean Absolute Deviation.
    The average absolute difference between each element in the dataset and the mean (average).
    MAD = sum((x - mean) ** 2) / len(numbers)
    return MAD

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Expected Output: 1.0
```
This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and calculates the Mean Absolute Deviation of that list using the formula `MAD = sum((x - mean) ** 2) / len(numbers)`. The example at the bottom demonstrates the function with a sample list of numbers.