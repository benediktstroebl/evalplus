```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

Alternatively, you could use the `statistics` module in Python's standard library to simplify the code:

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
    """
    mean = statistics.mean(numbers)
    absolute_differences = [abs(num - mean) for num in numbers]
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

Or, you could use a more concise version using list comprehension and the `statistics` module:

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
    """
    return statistics.mean(abs(num - statistics.mean(numbers)) for num in numbers)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```