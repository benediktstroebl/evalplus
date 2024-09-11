```python
from typing import List

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
        float: The Mean Absolute Deviation of the input numbers.

    Raises:
        ValueError: If the input list is empty.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences from the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad

# Example use case
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines the `mean_absolute_deviation` function, which takes a list of floating point numbers as input and returns their Mean Absolute Deviation. It first checks if the input list is empty, raising a ValueError if it is. Then it calculates the mean of the numbers, the absolute differences from the mean, and finally the Mean Absolute Deviation. The example use case at the end demonstrates how to use the function with a list of numbers.