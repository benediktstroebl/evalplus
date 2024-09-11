```python
from typing import List

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
        float: The Mean Absolute Deviation of the given list of numbers.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation for each number
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print("Mean Absolute Deviation:", result)
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input, calculates the Mean Absolute Deviation (MAD) and returns it. It uses list comprehension to calculate the absolute deviations from the mean and then averages these deviations to get the MAD. The example usage at the end shows how to use the function with a sample list of numbers.