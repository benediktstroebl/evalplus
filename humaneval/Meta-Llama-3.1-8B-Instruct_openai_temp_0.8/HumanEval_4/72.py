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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The mean absolute deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation for each number and sum them up
    absolute_deviations = sum(abs(num - mean) for num in numbers)

    # Calculate the mean absolute deviation
    mad = absolute_deviations / len(numbers)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

In this script:

1.  We first check if the input list `numbers` is not empty. If it is empty, we raise a `ValueError` because we cannot calculate the mean or MAD for an empty list.
2.  We calculate the mean of the input list by summing up all numbers and dividing by the count of numbers.
3.  We calculate the absolute deviation for each number by subtracting the mean from the number and taking the absolute value. We sum up these absolute deviations.
4.  We calculate the mean absolute deviation (MAD) by dividing the sum of absolute deviations by the count of numbers.
5.  Finally, we return the calculated MAD and demonstrate its usage with an example list `[1.0, 2.0, 3.0, 4.0]`.