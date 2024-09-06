Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    :return: Mean Absolute Deviation
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function called `mean_absolute_deviation()` that takes in a list of numbers and calculates the Mean Absolute Deviation (MAD), which is the average absolute difference between each element and the mean of the list. 

To improve efficiency, we utilized NumPy to handle operations with arrays, especially useful when dealing with multiple calculations. Finally, we provided a brief explanation of the math behind MAD. 

To ensure a balanced breadth-depth solution, I added comments to the code to explain the problem. 

You can further test this function by calling it with a list of numbers and comparing the result with manually calculated MAD values.