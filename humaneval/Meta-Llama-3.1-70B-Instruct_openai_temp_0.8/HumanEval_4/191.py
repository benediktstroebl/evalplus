```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

    The Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
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

Alternatively, you can use the `numpy` library to simplify the calculation:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

    The Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    # Convert the list to a numpy array
    arr = np.array(numbers)
    
    # Calculate the mean of the array
    mean = np.mean(arr)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = np.abs(arr - mean)
    
    # Calculate the mean of the absolute differences
    mad = np.mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Both scripts will calculate the Mean Absolute Deviation for the given list of numbers.