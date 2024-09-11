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
    float: The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script first calculates the mean of the input list, then it calculates the absolute deviation for each number in the list by subtracting the mean from each number and taking the absolute value. Finally, it calculates the mean of these absolute deviations, which is the Mean Absolute Deviation.