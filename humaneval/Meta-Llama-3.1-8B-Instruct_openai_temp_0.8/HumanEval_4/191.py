```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: A list of float numbers
    :return: The Mean Absolute Deviation of the input list
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check for an empty list
    if not numbers:
        raise ValueError("Input list is empty")
    
    mean = statistics.mean(numbers)  # Calculate the mean of the list
    return statistics.mean([abs(num - mean) for num in numbers])  # Calculate MAD

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns their Mean Absolute Deviation (MAD). It uses the `statistics` module to calculate the mean of the input list, and then calculates the MAD by finding the average absolute difference between each number and the mean. The script also includes an example usage at the end. 

This function raises a ValueError if the input list is empty, as the MAD is undefined in this case.