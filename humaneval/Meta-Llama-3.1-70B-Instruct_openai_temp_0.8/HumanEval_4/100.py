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
        numbers: A list of float numbers.

    Returns:
        The mean absolute deviation of the given list of numbers.
    """

    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we first calculate the mean of the input numbers using the `statistics.mean` function. Then, we use a list comprehension to calculate the absolute deviations from the mean for each number. Finally, we calculate the mean of these absolute deviations, which gives us the mean absolute deviation (MAD). The result is then returned by the function.

The example usage at the end demonstrates how to use the `mean_absolute_deviation` function with a sample list of numbers.