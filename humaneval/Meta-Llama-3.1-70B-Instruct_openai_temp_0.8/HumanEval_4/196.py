```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers: A list of float numbers.

    Returns:
    A float representing the Mean Absolute Deviation.
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty.")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function first checks if the input list is empty, then calculates the mean of the list. It then calculates the absolute deviations from the mean and finally calculates the mean of these deviations, which is the MAD. The result is returned as a float.

The script also includes an example usage of the function with the list `[1.0, 2.0, 3.0, 4.0]`, which produces the expected output of `1.0`.