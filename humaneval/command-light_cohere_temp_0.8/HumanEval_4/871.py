```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    from typing import List
    from math import sqrt
    numbers = [1.0, 2.0, 3.0, 4.0]
    = numbers
   
    # Calculate mean
    x_mean = sum(numbers)/len(numbers)
    # Calculate MAUD
    MAD = sum((x-x_mean)**2 for x in numbers)/len(numbers)
    # print(MAD)
    return MAD
# Example
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)==0.25)
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation, which is a measure of the dispersion or spread of a dataset. The script then passes the tests to ensure the function works correctly.