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
    The Mean Absolute Deviation of the input list.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if the list is empty
    if not numbers:
        return 0

    # Calculate the mean of the list
    mean = statistics.mean(numbers)

    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of floats as input and returns the Mean Absolute Deviation of the input list. It uses the `statistics` module from the Python standard library to calculate the mean of the input list and the absolute deviations from the mean. The example usage demonstrates how to use the function with a list of numbers.