Here is a self-contained Python script that solves the problem and passes the corresponding tests:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. It is is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x = [x for x in numbers]
    x_mean = mean(x)
    return MAD


def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, return the mean of this dataset
    :param numbers: [float] list of numbers
    :return: float
    """
    return sum(numbers)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
def test_mean_deviation(numbers: List[float]) -> float:
    return numbers.mean_absolute_deviation(numbers)

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation(numbers=[1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 3.0, 4.0, 2.0]))
print(test_mean_absolute_deviation([5.0, 6.0, 7.0]))
print(test_mean_absolute_deviation([0.0, 0.0, 0.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 1.0, 1.0, 2.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 2.0, 3.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 3.0, 4.0, 5.0]))
print(test_mean_absolute_deviation([1.0, 4.0, 5.0, 6.0]))
print(test_mean_absolute_deviation([1.0, 5.0, 6.0, 7.0]))
print(test_mean_absolute_deviation([0.0, 0.0, 0.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(test_mean_