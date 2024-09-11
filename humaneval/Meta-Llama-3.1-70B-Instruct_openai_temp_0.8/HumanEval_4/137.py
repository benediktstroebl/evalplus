```python
from typing import List
import statistics


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) for a given list of numbers.

    The Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """

    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script first calculates the mean of the input list using the `statistics.mean()` function. Then it calculates the absolute difference between each element and the mean using a list comprehension. Finally, it calculates the mean of the absolute differences using `statistics.mean()` again to get the Mean Absolute Deviation (MAD).