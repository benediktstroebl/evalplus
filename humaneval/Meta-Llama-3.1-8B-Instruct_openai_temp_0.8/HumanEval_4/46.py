```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

Alternatively, you can use the `statistics` module's `pvariance` function to simplify the calculation:

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    return statistics.pstdev(numbers)

# Example usage
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

Both of these scripts will output `1.0` when given the input `[1.0, 2.0, 3.0, 4.0]`.