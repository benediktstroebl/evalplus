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
        numbers (List[float]): A list of float numbers

    Returns:
        float: The Mean Absolute Deviation of the input list
    """
    if not numbers:  # check if the list is empty
        raise ValueError("Input list is empty")

    mean = statistics.mean(numbers)  # calculate the mean of the input list
    absolute_deviations = [abs(num - mean) for num in numbers]  # calculate absolute deviations from the mean
    mad = statistics.mean(absolute_deviations)  # calculate the mean of absolute deviations

    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # output: 1.0
print(mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]))  # output: 0.0
```

In this script, we use the `statistics` module from Python's standard library to calculate the mean of the input list. The `mean_absolute_deviation` function calculates the absolute deviations from the mean, and then returns the mean of these absolute deviations. If the input list is empty, a `ValueError` is raised.