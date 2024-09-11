```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the given dataset.

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation of the input dataset.
    """
    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can also write the function in a more concise way using the `statistics` module and a list comprehension:

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the given dataset.

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation of the input dataset.
    """
    mean = statistics.mean(numbers)
    return statistics.mean(abs(num - mean) for num in numbers)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```