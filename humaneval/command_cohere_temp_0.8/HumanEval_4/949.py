Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that takes in a list of numbers and calculates the mean absolute deviation (MAD) of the numbers in the list. 

The code first utilizes NumPy to bring the variable 'numbers' into a NumPy array for easier manipulation. It then finds the mean of the array through the `np.mean` method. Afterwards, it subtracts the mean from each value and takes the absolute value to obtain the deviation. The final step is to find the mean of the absolute deviations, returning the requested MAD. 

This solution has a time complexity of `O(n)` since it requires iterating over the list of numbers once to find the mean and once to find the absolute deviations from the mean.