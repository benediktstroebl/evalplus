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
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mean_absolute_deviation = statistics.mean(absolute_deviations)
    
    return mean_absolute_deviation

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns their Mean Absolute Deviation. It uses the `statistics` module from the Python standard library to calculate the mean of the input list and the list of absolute deviations. The function also includes a check to raise a `ValueError` if the input list is empty.