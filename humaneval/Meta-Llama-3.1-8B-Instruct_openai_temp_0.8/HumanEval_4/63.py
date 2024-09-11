### Mean Absolute Deviation Calculator
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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
In this script, the `mean_absolute_deviation` function takes a list of numbers as input, calculates the mean of the list, and then calculates the absolute deviation of each number from the mean. The average of these deviations is then returned as the Mean Absolute Deviation.