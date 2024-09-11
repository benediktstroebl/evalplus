```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers: A list of float numbers.

    Returns:
        Mean Absolute Deviation of the input list.
    """

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use the `numpy` library to simplify the implementation:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers: A list of float numbers.

    Returns:
        Mean Absolute Deviation of the input list.
    """

    # Convert the list to a numpy array
    numbers_array = np.array(numbers)
    
    # Calculate the mean of the input array
    mean = np.mean(numbers_array)
    
    # Calculate Mean Absolute Deviation
    mad = np.mean(np.abs(numbers_array - mean))
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Both scripts calculate the Mean Absolute Deviation of the input list by first calculating the mean, then calculating the absolute differences between each element and the mean, and finally calculating the mean of these absolute differences.