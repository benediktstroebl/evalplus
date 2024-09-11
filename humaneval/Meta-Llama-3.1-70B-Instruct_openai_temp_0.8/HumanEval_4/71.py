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
        float: The Mean Absolute Deviation of the input numbers.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input list contains non-numeric values.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Check if all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Input list must only contain numeric values")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diff = [abs(x - mean) for x in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diff) / len(absolute_diff)

    return mad


# Example use case:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```