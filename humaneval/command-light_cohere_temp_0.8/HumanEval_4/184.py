```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    """ Calculate the mean of a list of numbers """
    return sum(numbers)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
numbers = [1.0, 2.0, 3.0, 4.0]
def test(x):
    return x > 3.0

def test(numbers: List[float]):
    """ Test function """
    mean_value = mean(numbers)
    test_value = mean_absolute_deviation(numbers)
    print("Test passed!")
    assert mean_value == test_value

test([1.0, 2.0, 3.0, 4.0])
```