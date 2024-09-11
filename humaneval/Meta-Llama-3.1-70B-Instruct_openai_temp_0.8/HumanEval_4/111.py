```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a given dataset.

    Args:
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {result}")
```

This script first calculates the mean of the input dataset, then calculates the absolute difference between each element and the mean. Finally, it calculates the Mean Absolute Deviation by averaging these absolute differences. The result is printed to the console.

Note that this script includes a check to ensure the input list is not empty, raising a `ValueError` if it is. This helps prevent potential division-by-zero errors.