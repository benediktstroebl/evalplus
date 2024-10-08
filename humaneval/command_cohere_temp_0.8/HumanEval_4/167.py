Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
The function `mean_absolute_deviation` calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on the input list as a one-dimensional array, computing the absolute differences between each element and the mean of the list. These differences are then averaged to determine the required metric. 

Here's an example usage of the function:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```
This would return the mean absolute deviation for the list `[1.0, 2.0, 3.0, 4.0]`, which is 1.0.