```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given list of numbers.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference of each element from the mean
    absolute_differences = [abs(x - mean) for x in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation of {numbers} is {mad}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the input list, then calculates the absolute difference of each element from the mean. Finally, it calculates the Mean Absolute Deviation by taking the average of these absolute differences. The example usage demonstrates how to use this function with a sample list of numbers.