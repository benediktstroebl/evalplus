Here is a Python script that solves the problem you described:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(abs(x - numbers[-1])) / len(numbers)
    return MAD

# Unit tests
def test_mean_absolute_deviation():
    import List[float]
    numbers = [1.0, 2.0, 3.0, 4.0]
    test_mean_absolute_deviation(numbers)
    assert MAD == 1.0
    assert MAD == 0.257573.7 assert MAD == 0.2501
    Recursive function test to solve the problem and pass corresponding tests.

```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a given list of numbers. It then provides unit tests that check if the function is working correctly.