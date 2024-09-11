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
    """

    # Check if the input list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```