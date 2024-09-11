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
        numbers: A list of float numbers.

    Returns:
        Mean Absolute Deviation of the given numbers.

    Raises:
        ValueError: If the input list is empty.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the given numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_diff = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diff) / len(numbers)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we define the `mean_absolute_deviation` function that takes a list of float numbers as input. The function calculates the Mean Absolute Deviation (MAD) of the given numbers around their mean.

Here's a step-by-step explanation of the code:

1.  Check if the input list is empty and raise a `ValueError` if it is.
2.  Calculate the mean of the given numbers by summing them up and dividing by the count.
3.  Calculate the absolute difference between each number and the mean using a list comprehension.
4.  Calculate the Mean Absolute Deviation (MAD) by summing up the absolute differences and dividing by the count.
5.  Return the calculated MAD.

The script includes example usage and a docstring to provide documentation and usage information.