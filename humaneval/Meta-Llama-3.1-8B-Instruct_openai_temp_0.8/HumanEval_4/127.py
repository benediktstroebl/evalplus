### Mean Absolute Deviation Calculator
#### Python Script
```markdown
from typing import List
import statistics

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
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean_value = statistics.mean(numbers)

    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean_value) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This Python script uses the `statistics` module to calculate the mean of the input list and the mean of the absolute deviations. It also includes input validation to check if the input list is empty.