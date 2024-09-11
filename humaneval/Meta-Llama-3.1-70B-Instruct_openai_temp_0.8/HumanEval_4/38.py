```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)  # Output: 1.0
```