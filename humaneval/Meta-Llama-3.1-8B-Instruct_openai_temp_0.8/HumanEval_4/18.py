### Mean Absolute Deviation Calculator
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The mean absolute deviation of the given list.

    Examples:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    # Check if the input list is empty
    if not numbers:
        return 0

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each element and the mean
    abs_diffs = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences (MAD)
    mad = sum(abs_diffs) / len(abs_diffs)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It uses the formula `MAD = average | x - x_mean |`, where `x` is each element in the list and `x_mean` is the mean of the list. The function first checks if the input list is empty, and if so, returns 0. Otherwise, it calculates the mean of the list, the absolute differences between each element and the mean, and finally the mean of the absolute differences. The result is returned as a float. The example usage at the end demonstrates how to use the function with a sample list of numbers.