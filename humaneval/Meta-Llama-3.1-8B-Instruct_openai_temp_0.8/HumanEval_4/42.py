```markdown
## Mean Absolute Deviation Calculator
### Python Script to Calculate Mean Absolute Deviation

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {result}")
```

This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns the Mean Absolute Deviation of the input numbers. The function uses the formula for Mean Absolute Deviation, first calculating the mean of the input numbers, then calculating the absolute difference between each number and the mean, and finally calculating the mean of these absolute deviations. The example usage at the end demonstrates how to use the function with a sample list of numbers.