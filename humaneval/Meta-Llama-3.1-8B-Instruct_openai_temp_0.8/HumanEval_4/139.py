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
    if len(numbers) == 0:
        return 0.0  # Return 0 if the list is empty
    mean = statistics.mean(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return statistics.mean(absolute_deviations)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script uses the `statistics` module to calculate the mean of the input list, and then calculates the absolute deviations from the mean. Finally, it returns the mean of these absolute deviations, which is the Mean Absolute Deviation. If the input list is empty, it returns 0.0.