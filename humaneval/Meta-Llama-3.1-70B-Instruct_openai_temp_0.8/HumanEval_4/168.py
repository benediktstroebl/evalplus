```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.
    
    The MAD is the average absolute difference between each element and the mean of the dataset.
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference of each number from the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use the `numpy` library to simplify the calculation:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.
    
    The MAD is the average absolute difference between each element and the mean of the dataset.
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input numbers
    mean = np.mean(numbers)
    
    # Calculate the absolute difference of each number from the mean
    absolute_differences = np.abs(np.array(numbers) - mean)
    
    # Calculate the mean of the absolute differences
    mad = np.mean(absolute_differences)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```