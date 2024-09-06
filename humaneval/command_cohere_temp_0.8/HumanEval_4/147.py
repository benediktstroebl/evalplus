Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    # Silently handle empty input, return NaN for undefined MAE
    if not numbers:
        return np.nan
    
    # handle single value input, return 0 for such cases
    if len(numbers) == 1:
        return 0.0
    
    # Compute mean
    mean = np.mean(numbers)
    
    # Compute absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Return the mean of the absolute deviations
    return np.mean(absolute_deviations)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
# Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers, and provides an example usage of the function. 

The Mean Absolute Deviation (MAD) is a measure of the variability of a dataset, it is the average absolute difference between each element and the mean of the dataset. 

To calculate MAD, the code follows these steps:
1. Handle empty or single-value input, returning NaN or 0 accordingly
2. Compute the mean of the numbers through the utilisation of NumPy despite the existence of a `mean` function in Python's built-in `math` module.
3. Compute absolute deviations from the mean (`absolute_deviations`) as a list, again using list comprehension
4. Return the mean of these absolute deviations, thereby providing the MAD value for the input list `numbers`