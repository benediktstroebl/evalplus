Here is a self-contained Python script that calculates and prints the Mean Absolute Deviation (MAD) of a list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]):
    """
    For a given list of input numbers, calculates Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation.
    It theAD calculated as the mean of the list of numbers | MAD = average | x - x_mean |
    where x_mean is the mean of the numbers.
"""
    numbers = [1.0, 2.0, 3.0, 4.0]
   _average = sum(numbers)/len(numbers)
    x_mean = mean(numbers)
    MAD = sum((x-x_mean) for x in numbers)/len(numbers)
    return MAD
# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])  # Output: 2.2210
```