```python
from typing import List
import statistics


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    Args:
        numbers (List[float]): A list of numbers.
    Returns:
        float: The mean absolute deviation of the input list.
    """
    # Calculate the mean of the input list
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute deviation for each number
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean and then manually calculates the mean absolute deviation (MAD). The MAD is calculated as the average absolute difference between each element in the list and the mean of the list.