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
        float: The Mean Absolute Deviation.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage:
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    print(f"Mean Absolute Deviation of {numbers}: {mad}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the numbers, then calculates the absolute difference between each element and the mean, and finally calculates the mean of these absolute differences.

The script also includes example usage in the `if __name__ == "__main__":` block, which demonstrates how to use the function and prints the result.