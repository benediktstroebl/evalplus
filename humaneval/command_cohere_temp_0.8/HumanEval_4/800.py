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
This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the NumPy library to operate on arrays and perform calculations efficiently. 

Here's an example of using this function:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This would print:
```
1.0
```

Note that this implementation has a dependency on the `numpy` library, which is a robust addition for numerical operations in Python. However, it does increase the dependency footprint of this script. If you prefer a completely self-contained script, please let me know and I'll provide an alternative without external dependencies.