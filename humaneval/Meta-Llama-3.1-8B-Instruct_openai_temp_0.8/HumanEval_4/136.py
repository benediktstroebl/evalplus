### Mean Absolute Deviation Calculator
#### Python Implementation

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
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

In this script, we first calculate the mean of the input list using the `statistics.mean()` function. Then, we calculate the absolute deviation from the mean for each number in the list using a list comprehension. Finally, we calculate the mean of these absolute deviations to get the Mean Absolute Deviation.