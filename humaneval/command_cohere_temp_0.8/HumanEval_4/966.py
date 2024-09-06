Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.fsum(abs(num - mean(numbers)) for num in numbers) / len(numbers)

def mean(numbers: List[float]) -> float:
    return math.fsum(num for num in numbers) / len(numbers)

# Test code
assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
assert mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]) == 0.0
assert mean_absolute_deviation([1.0, -1.0, 2.0, -2.0, 3.0, -3.0]) == 2.0
```
This code includes a test suite to validate the correctness of the `mean_absolute_deviation()` function. You can easily incorporate more tests for different cases.