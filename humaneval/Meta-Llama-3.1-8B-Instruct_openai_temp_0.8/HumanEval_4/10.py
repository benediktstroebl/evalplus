### Mean Absolute Deviation Calculator

Here's a Python script that calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

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
    numbers (List[float]): A list of numbers to calculate MAD from.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the deviations (MAD)
    mad = statistics.mean(deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Note that I used the `statistics` module to simplify the calculation of the mean, which is not explicitly shown in the original function's docstring. This makes the code cleaner and more efficient.