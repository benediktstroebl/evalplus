Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script defines a function `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the numbers in the list. It uses the numpy array to operate the mathematical operations to calculate the mean and absolute deviation. 

This solution has a time complexity of `O(n)` since it requires iterating over the array once to calculate the mean, and another time to calculate the absolute deviation from the mean, which results in `O(n)` complexity.

Note that this assumes the list contains only numeric data. If the list contains non-numeric data, you may need additional handling. 
Let me know if you'd like me to explain any of the steps or concepts involved in this solution.  feel free to ask any questions.