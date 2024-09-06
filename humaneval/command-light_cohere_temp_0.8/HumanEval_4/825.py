```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """

    numbers = [1.0, 2.0, 3.0, 4.0]
   0)
   
    numbers = sorted(numbers)
    mean = sum(numbers)/len(numbers)
    mad = sum((x-mean)**2 for x in numbers) / len(numbers)
    return mad

# Test cases:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) # <.506253788

print(mean_absolute_deviation([4.5, 2.0, 2.0, 2.0])) 
print(mean_absolute_deviation([4.5, 6.0, 8.0, 6.0]))  #.4814541)
 print(mean_absolute_deviation([1.0, 1.0, 2.0, 2.0]))  #.4110.9
print(mean_absolute_deviation([2.0, 2.0, 3.0, 1.0])) ><.628515
 case < numbers = [1.5, 2.0, 2.0, 1.5] 
 print(mean_absolute_deviation([1.0, 2.0, 2.0, 2.0]))  #.68015342725.95)
 print(mean_absolute_deviation([1.0, 2.0, 3.0, 3.0]))  #.320519.35.

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  #.7416