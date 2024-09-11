```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) around the mean of a dataset.

    MAD is the average absolute difference between each element and the mean:
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    # First, calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Then, calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Finally, calculate the mean of these absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you could also implement this function using the `statistics` module and a list comprehension:

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) around the mean of a dataset.

    MAD is the average absolute difference between each element and the mean:
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    mean = statistics.mean(numbers)
    absolute_diffs = [abs(num - mean) for num in numbers]
    return statistics.mean(absolute_diffs)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Or with the `numpy` library, it can be done even more concisely:

```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) around the mean of a dataset.

    MAD is the average absolute difference between each element and the mean:
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(numbers)))

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```