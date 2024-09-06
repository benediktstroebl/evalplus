Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1.0, 2.0, 3.0, 4.0]
mean_deviation = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation for {numbers}: {mean_deviation}")

```

This script defines the `mean_absolute_deviation` function that takes a list of numbers as input and returns the mean absolute deviation of the numbers. It uses NumPy to calculate the mean and absolute deviations efficiently.

The printed test result reveals that the mean absolute deviation for the list `[1.0, 2.0, 3.0, 4.0]` is `1.0`.