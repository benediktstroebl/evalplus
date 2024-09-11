```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of a given list of numbers.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script first calculates the mean of the input list, then calculates the absolute difference between each element and the mean. Finally, it calculates the mean of the absolute differences, which is the Mean Absolute Deviation. The result is then printed to the console. If the input list is empty, a ValueError is raised.