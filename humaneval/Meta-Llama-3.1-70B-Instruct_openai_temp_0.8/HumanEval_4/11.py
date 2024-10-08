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
        numbers: A list of float numbers.
    
    Returns:
        A float representing the Mean Absolute Deviation.
    
    Raises:
        ValueError: If the input list is empty.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use NumPy to calculate the Mean Absolute Deviation in a more concise way:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers: A list of float numbers.
    
    Returns:
        A float representing the Mean Absolute Deviation.
    
    Raises:
        ValueError: If the input list is empty.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Convert the input list to a NumPy array
    numbers = np.array(numbers)
    
    # Calculate the Mean Absolute Deviation
    mad = np.mean(np.abs(numbers - np.mean(numbers)))
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```