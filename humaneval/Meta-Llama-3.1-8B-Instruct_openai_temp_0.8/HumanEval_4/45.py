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
        float: The Mean Absolute Deviation of the given numbers.
    """
    if not numbers:
        raise ValueError("Input list is empty")

    mean = statistics.mean(numbers)
    deviation = [abs(x - mean) for x in numbers]
    return statistics.mean(deviation)


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. The Mean Absolute Deviation is the average absolute difference between each number and the mean of the entire dataset. If the input list is empty, it raises a `ValueError`. The script includes example usage of the function with a list of numbers.