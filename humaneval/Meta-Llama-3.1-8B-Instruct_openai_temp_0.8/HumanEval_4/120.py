### Mean Absolute Deviation Calculator
#### Code

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
    numbers (List[float]): A list of numbers

    Returns:
    float: The Mean Absolute Deviation

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

#### Explanation

This Python script defines a function called `mean_absolute_deviation` that takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) for this list. The MAD is calculated as the average absolute difference between each element and the mean of the dataset.

The function uses the `statistics` module from the Python Standard Library to calculate the mean of the input list and the mean of the absolute deviations. The absolute deviation from the mean for each number is calculated using a list comprehension.

The script includes an example usage of the `mean_absolute_deviation` function with a list of numbers `[1.0, 2.0, 3.0, 4.0]`, which outputs `1.0` as expected.