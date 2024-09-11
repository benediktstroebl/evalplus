### Mean Absolute Deviation Calculator
#### Python Script

```markdown
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Initialize a variable to store the sum of absolute deviations
    absolute_deviations = 0

    # Iterate over the input list
    for num in numbers:
        # Calculate the absolute deviation from the mean
        absolute_deviation = abs(num - mean)
        # Add it to the total sum
        absolute_deviations += absolute_deviation

    # Calculate the Mean Absolute Deviation
    mad = absolute_deviations / len(numbers)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation for a given list of numbers. It then demonstrates how to use this function with an example input list.