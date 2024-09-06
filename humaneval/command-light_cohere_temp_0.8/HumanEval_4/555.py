```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    #Calculate Mean Absolute Deviation
    MAD = math.absolute(sum(map(lambda x: abs(x - numbers[-1]))) / len(numbers))
    return MAD

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)
print(mean_absolute_deviation([2.0, 2.0, 3.0, 4.0] == 0.0)
print(mean_absolute_deviation([4.0, 2.0, 2.0, 4.0] == 1.0)
print(mean_absolute_deviation([4.0, 1.0, 1.0, 4.0] == 0.25 print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0] == 0.0))
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0] == 0.25)
 print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0] == 0.8))
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0] == 0.4)
 print(mean_absolute_deviation([1.0, 3.0, 4.0] == 0.2))
 print(mean_absolute_deviation([1.0, 2.0, 4.0, 4.0] == 0.2)
 print(mean_absolute_deviation([1.0, 2.0, 2.0, 3.0] == 0.2))
 print(mean_absolute_deviation([2.0, 1.0, 2.0] == 0.0) ) print(mean_absolute_deviation([2.0, 2.0, 2.0, 3.0] == 0.6))
 print(mean_absolute_deviation([2.0, 2.0, 2.0] == 0.8) ) print(mean_absolute_deviation([3.0, 3.0, 4.0] == 0.4)
 print(mean_absolute_deviation([4.0, 3.0, 4.0] == 0.2))
 print(mean_absolute_deviation([5.0, 4.0, 3.0] == 0.0) 
 print(mean_absolute_deviation([5.0, 4.0, 3.0, 5.0] == 0.2))
 print(mean_absolute_deviation([6.0, 5.0, 6.0] == 0.4) 
 print(mean_absolute_deviation([6.0, 6.0, 6.0] != 0.6))