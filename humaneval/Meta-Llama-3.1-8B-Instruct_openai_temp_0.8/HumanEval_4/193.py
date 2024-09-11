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
    # Check if list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script first checks if the input list is empty, and raises a ValueError if it is. It then calculates the mean of the numbers using the built-in sum function. The absolute deviations from the mean are calculated using a list comprehension, and the mean of these deviations is calculated using the built-in sum function again. The result is then returned as the Mean Absolute Deviation.