```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

Alternatively, you can use the `statistics` module to simplify the calculation:

```python
import statistics
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

Or even shorter using list comprehension and the `statistics` module:

```python
import statistics
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    
    # Calculate the mean absolute deviation
    mad = statistics.mean([abs(x - statistics.mean(numbers)) for x in numbers])
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```