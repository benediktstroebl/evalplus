### Mean Absolute Deviation (MAD) Calculator
#### Problem Statement
Calculate the Mean Absolute Deviation (MAD) for a given list of numbers.

#### Solution
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
        float: The Mean Absolute Deviation.
    """
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of these absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script first calculates the mean of the input numbers using the `statistics.mean()` function. It then calculates the absolute deviation of each number from the mean and finally computes the mean of these absolute deviations.