### Mean Absolute Deviation Calculator
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
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the average of the deviations (Mean Absolute Deviation)
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the numbers, then calculates the absolute deviation of each number from the mean, and finally returns the average of these deviations. The example usage at the end demonstrates how to use this function with a sample list of numbers.