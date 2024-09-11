```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.
    """

    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences from the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use the numpy library to simplify the calculation:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.
    """

    # Convert the list to a numpy array
    arr = np.array(numbers)
    
    # Calculate the mean and absolute differences in one step
    mad = np.mean(np.abs(arr - np.mean(arr)))
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```