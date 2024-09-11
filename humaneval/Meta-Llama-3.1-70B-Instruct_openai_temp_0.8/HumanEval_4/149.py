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
        numbers: A list of floating point numbers.

    Returns:
        A float representing the mean absolute deviation.
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0


# Alternative implementation using numpy
import numpy as np

def mean_absolute_deviation_numpy(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset using numpy.
    """
    mean = np.mean(numbers)
    mad = np.mean(np.abs(np.array(numbers) - mean))
    return mad


# Test the numpy implementation
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation_numpy(numbers))  # Output: 1.0
```