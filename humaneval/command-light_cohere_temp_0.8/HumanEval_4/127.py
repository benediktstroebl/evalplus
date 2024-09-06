Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    # initialize variables
    mean = sum(numbers)/len(numbers)
    x = 0
    for num in numbers:
        x += math.abs(num - mean)
    # return the mean of the absolute deviations
    return x / len(numbers)
``` 
This function uses the Mean Absolute Deviation formula to calculate the Mean Absolute Deviation around the mean of the dataset.

Note that this function is self-contained, and does not require any external variables or functions to be defined.