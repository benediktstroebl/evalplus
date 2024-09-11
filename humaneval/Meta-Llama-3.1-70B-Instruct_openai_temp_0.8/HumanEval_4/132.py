```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    Args:
        numbers (List[float]): A list of input numbers.
    Returns:
        float: Mean Absolute Deviation.
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")  # Output: Mean Absolute Deviation: 1.0
```

Alternatively, you can use a one-liner with a list comprehension and the `statistics` module:

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    Args:
        numbers (List[float]): A list of input numbers.
    Returns:
        float: Mean Absolute Deviation.
    """
    return statistics.mean([abs(num - statistics.mean(numbers)) for num in numbers])


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")  # Output: Mean Absolute Deviation: 1.0
```