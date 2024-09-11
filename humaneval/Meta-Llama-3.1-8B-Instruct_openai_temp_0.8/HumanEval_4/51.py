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
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This script uses the `statistics` module to calculate the mean of the input list, and then calculates the absolute deviations from the mean using a list comprehension. The `mean` function from `statistics` is then used to calculate the mean of these deviations, which is the Mean Absolute Deviation (MAD). 

However, since we are using `statistics.mean()` which is essentially doing the same operation 3-4 times (C.O.N.S.T.A.N.T) when you are dealing with multiple lists to calculate the MAD; you can instead calculate the MAD directly using the formula as follows:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the MAD by summing the deviations and dividing by the count
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

In the code above, I have directly used the `sum()` function to calculate the sum of all numbers and the sum of the absolute deviations, which is more efficient than using the `statistics.mean()` function twice.