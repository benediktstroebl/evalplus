```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the given dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
    numbers (List[float]): A list of input numbers.

    Returns:
    float: The Mean Absolute Deviation of the given dataset.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    # Calculate the mean of the given list of numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we define a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first checks if the list is empty and raises a `ValueError` if it is. Then, it calculates the mean of the list, the absolute differences between each number and the mean, and finally, the Mean Absolute Deviation. The function returns the calculated Mean Absolute Deviation. The example usage at the end demonstrates how to use the function with a sample list of numbers.