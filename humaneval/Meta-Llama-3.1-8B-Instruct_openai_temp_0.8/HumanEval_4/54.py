### Mean Absolute Deviation Calculator
#### Python Script
```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean of a dataset.
    
    Parameters:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean_value = statistics.mean(numbers)

    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean_value) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) around the mean of the dataset. The MAD is calculated using the `statistics` module, which provides functions for calculating mathematical statistics of numeric data. The example usage at the end demonstrates how to call the function with a list of numbers and print the result.