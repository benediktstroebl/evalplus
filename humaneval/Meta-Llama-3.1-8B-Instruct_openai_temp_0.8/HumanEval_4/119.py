### Mean Absolute Deviation Calculator
#### A Python Script to Calculate the Mean Absolute Deviation of a Dataset

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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module's `mean` function to calculate the mean of the input list and then uses a list comprehension to calculate the absolute deviations from the mean for each number. The mean of these absolute deviations is then calculated and returned as the Mean Absolute Deviation.