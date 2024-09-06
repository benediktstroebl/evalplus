Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
num = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(num))
```
This script includes a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on arrays, compute the mean, and calculate the absolute deviations. The function is then tested using pytest with a sample input list of numbers. The example usage demonstrates how to use the function with a sample list of numbers.