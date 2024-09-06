```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset"""
    mad = []
    numbers.append(0.0)
   >  # first element of the dataset
    mad.append(numbers[0])
    for num in numbers[1:]:
        mad.append(num - num - num - num)
    mad = [a + b for a, b in zip(mad, numbers)]
    return math.sqrt(sum(mad) / len(numbers))

def test_mean_absolute_deviation(numbers: List[float]) -> None:
    assert mean_absolute_deviation(numbers) == 0.1
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 0.25
    assert mean_absolute_deviation([10.0, 20.0, 30.0]) == 6.25 assert mean practice_ absolute_deviation([0.5, 0.0, 1.0]) == 0.25 assert mean object+ absolute_deviation([5.5, 4.0, 0.0, 3.0]) == 0.1

print("Pass all tests!")
```