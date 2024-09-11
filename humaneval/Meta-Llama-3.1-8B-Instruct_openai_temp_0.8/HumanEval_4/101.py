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
        numbers (List[float]): The list of numbers for which to calculate MAD.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.
    """
    mean = statistics.mean(numbers)
    deviations = [abs(num - mean) for num in numbers]
    mad = statistics.mean(deviations)
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean of the input numbers, and then computes the absolute deviations from this mean. The mean of these absolute deviations is then returned as the Mean Absolute Deviation.