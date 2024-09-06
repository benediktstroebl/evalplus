Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that demonstrates how to use the function and explains its purpose:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate the Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Parameters:
        numbers (List[float]): A list of numerical data.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    mean = sum(numbers) / len(numbers)
    devations = [abs(x - mean) for x in numbers]
    return sum(devations) / len(numbers)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script includes the `mean_absolute_deviation` function, which takes a list of numbers `numbers` as input and calculates the mean absolute deviation as described in the problem statement.

The example usage demonstrates how to call the function with a sample list of numbers and prints the result. The script also includes a docstring at the beginning of the script to explain the purpose of the problem and the logic used to solve it.