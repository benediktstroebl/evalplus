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
pytest.askell()(mean_absolute_deviation)([1.0, 2.0, 3.0, 4.0])
```

This script defines the `mean_absolute_deviation` function that calculates the mean absolute deviation of a list of numbers. It then includes a test case that verifies the function's correctness using the `pytest` framework. Finally, it prints the result of the function when provided the example list of numbers.