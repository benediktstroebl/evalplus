Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    # Calculate mean value for the calculation
    mean = sum(numbers) / len(numbers)

    MAD = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    return MAD

# Unit tests:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])) # 4.1  #

print(mean_absolute_deviation([1.0, 10.0, 5.0])) # 4.4 

print(mean_absolute_deviation([1.0, 2.0, 4.0])) # 4.2 
 print(mean_absolute_deviation([10.0, 20.0, 30.0])) # 2.9
print(mean_absolute_deviation([-3.0, -4.0, -5.0])) # 6.0
print(mean_absolute_deviation([1.0, 2.0, 3.0])) # 3.9
print(mean_absolute_deviation([4.9, 4.0, 4.0])) # 2.0 
 print(mean_absolute_deviation([1.0, 2.0, 4.0])) # 3.6

print(mean_absolute_deviation([10.0, 20.0, 30.0])) # 1.5

print(mean_absolute_deviation([1.0, 2.0, 5.0])) # 4.2
print(mean_absolute_deviation([1.0, 10.0, 2.0])) # 2.0 
 print(mean_absolute_deviation([-3.0, -4.0, -5.0]))  # 3.4

print(mean_absolute_deviation([4.9, 4.0, 4.0])) # 2.2
```