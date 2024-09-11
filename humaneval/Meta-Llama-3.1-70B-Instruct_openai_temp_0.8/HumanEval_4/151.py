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
    A floating point number representing the Mean Absolute Deviation.
    """
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Expected output: 1.0

# Alternative solution using NumPy library
import numpy as np

def mean_absolute_deviation_alternative(numbers: List[float]) -> float:
    """
    Alternative implementation using NumPy library.
    """
    numbers_array = np.array(numbers)
    return np.mean(np.abs(numbers_array - np.mean(numbers_array)))

print(mean_absolute_deviation_alternative([1.0, 2.0, 3.0, 4.0]))  # Expected output: 1.0
```