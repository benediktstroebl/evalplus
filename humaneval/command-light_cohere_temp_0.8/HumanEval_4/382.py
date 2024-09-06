Here's the solution to the problem in a self-contained Python script:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(x - numbers[-1]) / len(numbers) - 1
    return MAD

def test_mean_absolute_deviation(numbers: List[float]) ->  # Tests the function
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0
assert mean mean_absolute_deviation([5.0, 4.0, 3.0]) == 3.0
assert mean_mean_absolute_deviation([10.0, 20.0, 30.0]) == 7.0
print('Test passed all tests.')
```