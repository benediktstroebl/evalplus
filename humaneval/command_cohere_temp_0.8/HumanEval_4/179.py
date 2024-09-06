Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script utilizes the `numpy` library, alongside the `math` library to calculate the Mean Absolute Deviation of a list of numbers. The function `mean_absolute_deviation` takes a list of numbers and returns the mean absolute deviation of the list, which is the average absolute difference between each element and the mean of the list. 

Here's an example of using this function:
```python
print(f"The mean absolute deviation of [1.0, 2.0, 3.0, 4.0] is {mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])}")
```
This would output the following:
```
The mean absolute deviation of [1.0, 2.0, 3.0, 4.0] is 1.0
``` 

This demonstrates that the code works as described in the prompt.