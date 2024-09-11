```python
from typing import List
import statistics  # Importing the statistics module for calculating mean


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of float numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the given list of numbers.
    """
    numbers = [num for num in numbers if not isinstance(num, str)]  # Remove potential string values
    mean_value = statistics.mean(numbers)  # Calculate the mean of the numbers
    absolute_deviations = [abs(num - mean_value) for num in numbers]  # Calculate the absolute deviations
    mad = statistics.mean(absolute_deviations)  # Calculate the mean of the absolute deviations
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script takes a list of numbers, calculates the mean of the list, calculates the absolute difference between each number and the mean, and then calculates the mean of these absolute differences to get the Mean Absolute Deviation. It handles potential string values in the list by removing them before calculation.