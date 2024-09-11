### Mean Absolute Deviation Calculator

The following Python script calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The mean absolute deviation of the input list.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input, calculates the mean of the numbers, and then calculates the mean of the absolute differences between each number and the mean. The result is returned as the mean absolute deviation. The example usage demonstrates how to use the function with a sample list of numbers.