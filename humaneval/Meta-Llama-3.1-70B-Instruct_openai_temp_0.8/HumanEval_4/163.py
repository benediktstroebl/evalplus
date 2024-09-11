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
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input dataset.

    Raises:
    ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input dataset
    mean = statistics.mean(numbers)

    # Calculate the absolute deviation of each element from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the input dataset using the `statistics.mean` function. Then, it calculates the absolute deviation of each element from the mean using a list comprehension. Finally, it calculates the mean of the absolute deviations to obtain the MAD. The function raises a `ValueError` if the input list is empty. The script includes an example usage of the function with a list of numbers.