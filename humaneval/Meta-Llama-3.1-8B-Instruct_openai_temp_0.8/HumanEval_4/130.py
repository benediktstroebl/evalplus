### Mean Absolute Deviation Calculator
#### A Python Script to Calculate the Mean Absolute Deviation

```markdown
### Requirements
This script uses the `typing` module for type hints.

### Code
```python
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
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the given numbers
    mean = statistics.mean(numbers)
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    # Calculate the mean of the absolute deviations (MAD)
    mad = statistics.mean(deviations)
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation
This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input. It calculates the mean of the numbers, then calculates the absolute deviations from the mean. Finally, it calculates the mean of the absolute deviations, which is the Mean Absolute Deviation. The function returns the MAD.

The script also includes an example usage of the function with the list `[1.0, 2.0, 3.0, 4.0]`, which prints the result `1.0` to the console.
```