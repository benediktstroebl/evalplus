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
        numbers: A list of numbers.

    Returns:
        The Mean Absolute Deviation.
    """
    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script uses list comprehension to calculate the absolute differences between each element and the mean, and then uses the `statistics.mean` function to calculate the mean of these differences. The result is the Mean Absolute Deviation.