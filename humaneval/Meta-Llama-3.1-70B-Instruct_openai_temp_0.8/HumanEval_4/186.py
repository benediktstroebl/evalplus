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
    float: The Mean Absolute Deviation of the input numbers.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    print(f"Mean Absolute Deviation of {numbers}: {mad}")
```

This script calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the numbers, then calculates the absolute differences between each number and the mean, and finally calculates the average of these absolute differences. The example usage at the end demonstrates how to use the `mean_absolute_deviation` function.