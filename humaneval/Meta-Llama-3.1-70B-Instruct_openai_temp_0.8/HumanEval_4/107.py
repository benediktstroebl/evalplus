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
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.

    Raises:
    ValueError: If the input list is empty.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)  # Output: 1.0
```

In this code:

*   We first check if the input list is empty and raise a ValueError if it is.
*   We calculate the mean of the input list by summing all the numbers and dividing by the count of numbers.
*   We calculate the absolute difference between each number and the mean using a list comprehension.
*   We calculate the Mean Absolute Deviation by summing the absolute differences and dividing by the count of numbers.

This code follows the problem's requirements and provides a clear example usage at the end.