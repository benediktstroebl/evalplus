### Mean Absolute Deviation Calculator
```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script calculates the Mean Absolute Deviation of a given list of numbers. It uses the built-in `statistics` module to calculate the mean of the list, and then calculates the absolute differences between each number and the mean. The Mean Absolute Deviation is then calculated as the average of these absolute differences.