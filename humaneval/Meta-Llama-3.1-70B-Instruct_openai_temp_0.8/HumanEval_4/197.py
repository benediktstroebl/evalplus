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
        float: The Mean Absolute Deviation of the input list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = statistics.mean(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_diffs)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

In this script, we first calculate the mean of the input list using the `statistics.mean` function. Then, we calculate the absolute differences between each number and the mean using a list comprehension. Finally, we calculate the mean of these absolute differences, which is the Mean Absolute Deviation.

The script also includes error handling to raise a `ValueError` if the input list is empty. The example usage at the end demonstrates how to use the `mean_absolute_deviation` function with a sample list of numbers.