Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that demonstrates how to use the function and explains its purpose:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate the Mean Absolute Deviation
    around the mean of the dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Parameters:
        numbers (List[float]): A list of numerical data.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    mean = sum(numbers) / len(numbers)
    deviation = sum(abs(x - mean) for x in numbers)
    return deviation / len(numbers)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script includes the `mean_absolute_deviation` function that takes a list of numerical data (`List[float])` as input and calculates the mean absolute deviation as described in the problem statement.

The MD code block describes the purpose of the function and provides an example usage with a test case.