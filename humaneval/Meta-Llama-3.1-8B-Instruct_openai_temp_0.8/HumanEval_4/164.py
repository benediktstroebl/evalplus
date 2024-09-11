```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

However, this can be further improved using the `numpy` library which provides a vectorized implementation of the mean and absolute deviation calculations, making it more efficient for large datasets:

```python
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    # Convert the input list to a numpy array
    numbers = np.array(numbers)

    # Check if the input array is empty
    if len(numbers) == 0:
        raise ValueError("Input array cannot be empty")

    # Calculate the mean of the dataset
    mean = np.mean(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = np.abs(numbers - mean)

    # Calculate the mean of the absolute deviations
    mad = np.mean(absolute_deviations)

    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

Both of these scripts will output `1.0` when given the input `[1.0, 2.0, 3.0, 4.0]`.