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
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the list
    mean = statistics.mean(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # Return the average of the absolute deviations
    return statistics.mean(absolute_deviations)

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The MAD is calculated as the average absolute difference between each element in the list and the mean of the list. The function uses the `statistics` module to calculate the mean of the list. It also includes a check to ensure that the input list is not empty.