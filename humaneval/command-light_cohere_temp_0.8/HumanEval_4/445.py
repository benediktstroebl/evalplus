Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean | 
    where x is each element in the input list and x_mean is the mean of the list.
    return the mean value of MAD
    """
    return math.abs(mean(numbers, mean(numbers)))
```

This code defines a function `mean_absolute_deviation` which takes a list of numbers as input and returns the Mean Absolute Deviation of this dataset, calculated using the `math.abs()` function. The `mean()` function is used to calculate the mean of the input list. 

Please note that this code is self-contained, and you can use it to solve the problem without using external libraries.