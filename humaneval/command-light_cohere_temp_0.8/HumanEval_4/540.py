Here is a Python script that defines a self-contained function to solve the problem:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of this dataset
    """
    numbers.append(0.0)  # float(len(numbers) + 1)
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Unit Tests
def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 0.2510
0.7

def test_mean_absolute_deviation_with_bad_input():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 2.5629
2
4

def test_mean_absolute_deviation_with_high_input():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

0