### Calculating Mean Absolute Deviation

```python
from typing import List
import numpy as np

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
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Use numpy's mean function to calculate the mean of the list
    mean_x = np.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(x - mean_x) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = np.mean(absolute_diffs)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use a more concise implementation using NumPy:

```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(numbers)))

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```