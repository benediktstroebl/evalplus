Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. This is done using the `numpy` library to handle the array operations and calculations of the mean and absolute deviations.

To ensure correctness, the function is designed to be self-contained and optimally utilizes the `numpy` library, which is widely used for numerical operations in Python.