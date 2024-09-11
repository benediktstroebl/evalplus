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
    
    :param numbers: A list of float numbers
    :return: The Mean Absolute Deviation of the input list
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the given list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each element and the mean
    abs_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of these absolute differences
    mad = statistics.mean(abs_diffs)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this code:

1.  We first import the necessary `statistics` module for mean calculation.
2.  The function `mean_absolute_deviation` takes a list of float numbers as input.
3.  It calculates the mean of the input list using the `statistics.mean` function.
4.  Then, it calculates the absolute differences between each element and the mean using a list comprehension.
5.  Finally, it calculates the mean of these absolute differences using `statistics.mean` again.
6.  The result is returned as the Mean Absolute Deviation (MAD) of the input list.

Note: This code includes input validation to raise a `ValueError` when the input list is empty.