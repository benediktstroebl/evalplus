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
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference of each element from the mean
    absolute_diff = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diff) / len(absolute_diff)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

Alternatively, you can use the `numpy` library to make the code more concise:

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
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Convert the list to a numpy array
    numbers = np.array(numbers)
    
    # Calculate the Mean Absolute Deviation using numpy functions
    mad = np.mean(np.abs(numbers - np.mean(numbers)))
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```