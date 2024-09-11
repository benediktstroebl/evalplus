```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers: A list of float numbers.

    Returns:
        The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function uses the `statistics` module to calculate the mean of the input numbers and then calculates the absolute difference between each number and the mean. Finally, it calculates the mean of these absolute differences to get the MAD.

You can run this script with the provided example usage to see the output. The `numbers` list is passed to the `mean_absolute_deviation` function, and the result is printed to the console.