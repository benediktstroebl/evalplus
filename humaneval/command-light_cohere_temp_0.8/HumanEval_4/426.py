```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Compute the Mean Absolute Deviation, which is the average absolute difference 
    between each element and the mean. 
    >>> Mean Absolute Deviation is a measure of how far the data points 
    deviate from the mean. 
    ## Step 1: Initialize the variables 
    mean = sum(numbers) / len(numbers)
    x_mean = mean 
    mad = 0.0
    ## Step 2: Compute the average absolute 
    difference between each element and the mean 
    for x in numbers:
        mad += abs(x - mean)
    mad = mad / len(numbers)
    # Step 3: Return the computed Mean Absolute Deviation 
    return mad
# Example usage 
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)))
```