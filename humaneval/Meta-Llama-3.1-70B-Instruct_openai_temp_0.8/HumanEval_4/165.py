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
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input dataset.
    """
    # Calculate the mean of the input dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use the `statistics` module to simplify the calculation:

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
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input dataset.
    """
    # Calculate the mean of the input dataset
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Or even more concisely:

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
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input dataset.
    """
    mean = statistics.mean(numbers)
    return statistics.mean(abs(x - mean) for x in numbers)


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```