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
        float: The mean absolute deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the deviations (Mean Absolute Deviation)
    mad = sum(deviations) / len(deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This code first calculates the mean of the input list of numbers. It then calculates the absolute deviation from the mean for each number, and finally calculates the mean of these deviations to find the Mean Absolute Deviation (MAD). The example use case demonstrates how to use this function with a sample list of numbers.