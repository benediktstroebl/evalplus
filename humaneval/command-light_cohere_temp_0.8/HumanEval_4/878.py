```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = math.abs(sum(x[i] - mean) / len(numbers))
    return MAD


# Test cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.25)
numbers = [10.0, 10.0, 10.0, 10.0]
print(mean_absolute_deviation(numbers) == 0.0)
numbers = [1.0, 10.0, 10.0, 10.0]
print(mean_absolute_deviation(numbers) == 4.0)
numbers = [1.0, 10.0, 1.0, 10.0]
print(mean_absolute_deviation(numbers) == 0.0) or small_numbers = [0.0, 0.0]
print(mean_absolute_deviation(small_numbers) == 0.0)
print(mean_absolute_deviation([5.0, 4.0]) == 0.1)
print(mean_absolute_deviation([10.0, 0.0, 10.0, 0.0]) == 0.0)
 print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 2.0)
 print(mean_absolute_deviation([2.0, 1.0, 1.0, 2.0]) == 0.0)
 print(mean_absolute_deviation([2.0, 1.0, 1.0, 2.0]) == 0.0)
 print(mean_absolute_deviation([3.0, 4.0, 1.0, 5.0]) == 0.6)
 print(mean_absolute_deviation([5.0, 4.0, 2.0, 3.0]) == 0.16)
 print(mean_absolute_deviation([6.0, 7.0, 6.0, 8.0]) == 0.4)
 print(mean_absolute_deviation([7.0, 6.0, 7.0, 8.0])) == 0.44
print(mean_absolute_deviation([8.0, 8.0, 8.0, 8.0])) == 0.24
print(mean_absolute_deviation([9.0, 9.0, 9.0, 9.0])) == 0.36
print(mean_absolute_deviation([10.0, 10.0, 10.0, 10.0])) == 0.16
print(mean_absolute_deviation([10.0, 10.0, 1.0, 10.0])) == 0.16
print(mean_absolute_deviation([11.0, 11.0, 11.0, 11.0])) == 0.12
print(mean_absolute_deviation([12.0, 12.0, 12.0, 12.0])) == 0.08
print(mean_absolute_deviation([12.0, 12.0, 12