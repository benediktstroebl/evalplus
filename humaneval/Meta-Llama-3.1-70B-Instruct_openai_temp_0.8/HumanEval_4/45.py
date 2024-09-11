```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.

    Raises:
    ValueError: If the input list is empty.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation of {numbers} is: {mad}")
```

In this script, we define a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) around the mean of the dataset. The function first checks if the input list is empty, then calculates the mean of the numbers, the absolute differences between each element and the mean, and finally the mean of the absolute differences.

The example usage shows how to use the function with a list of numbers and print the result.