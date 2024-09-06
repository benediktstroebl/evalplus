```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculates the Mean Absolute Deviation around the mean of this dataset
    MAD = sum(x - mean) ** 2 / len(numbers)
    return MAD


def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    same a test_mean_absolute_deviation(numbers)
    assert MAD == 0.25
    assert MAD > 0.0
    assert MAD < 1.25 assert MAD != 1.0
   0
   es that the Mean Absolute Deviation calculation is correct