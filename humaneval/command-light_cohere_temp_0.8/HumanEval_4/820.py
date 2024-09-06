Here's the solution for your prompt:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation.
    MAD = average | x -x_mean |
    
    where x and x_mean are each element in the input list numbers.
    """
    
    assert len(numbers) == len(set(numbers)), "Input list must be unique."
    assert all(type(x) == float for x in numbers), "Input list must be float values."
    assert all(numbers), "Input list cannot be empty."
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each element from the mean
    mad = sum((x - mean) ** 2) / len(numbers)
    
    return mad
```

This script uses the Mean Absolute Deviation (MAD) formula to calculate the absolute deviation between each number in a list and the mean of the numbers.

It also includes input validation tests to ensure that the input is a list of unique float values, all values are of the same data type (float), and the input list is not empty.