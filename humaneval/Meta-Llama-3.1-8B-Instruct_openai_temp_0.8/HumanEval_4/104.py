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
        numbers (List[float]): A list of numbers

    Returns:
        float: The Mean Absolute Deviation of the input list
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This Python script defines the `mean_absolute_deviation` function, which calculates the Mean Absolute Deviation (MAD) of a list of numbers. The MAD is a measure of the average distance between each number in the list and the mean of the list.

The function uses the `statistics` module to calculate the mean of the input list and the mean of the absolute deviations. It then returns the MAD.

The example usage at the end demonstrates how to use the function to calculate the MAD of the list `[1.0, 2.0, 3.0, 4.0]`. When run, it prints `1.0`.