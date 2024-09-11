```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)
    
    return mad
```

You can use this function as follows:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0

numbers = [5.0, 5.0, 5.0, 5.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 0.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. It first calculates the mean of the numbers, then calculates the absolute deviations of each number from the mean, and finally calculates the mean of these deviations. If the input list is empty, it raises a `ValueError`.