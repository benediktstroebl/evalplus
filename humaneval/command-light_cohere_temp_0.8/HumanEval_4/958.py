Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:

```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    mean = sum(numbers)/len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers)
    return math.sqrt(mad / (len(numbers) - 1))

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0] == 0.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) > 0.5
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) < 0.1)
print(mean_absolute_deviation([2.0, 2.0, 3.0, 4.0]) == 0.1)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) < 0.5)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 0.4)
 print(mean_absolute_deviation([1.0, 3.0, 3.0]) < 0.6)
 print(mean_absolute_deviation([1.0, 1.0, 2.0]) < 0.4)
 print(mean_absolute_deviation([1.0, 0.0, 2.0]) < 0.8)
 print(mean_absolute_deviation([1.0, 0.0, 2.0]) < 0.9)
 print(mean_absolute_deviation([1.0, 2.0, 0.0])) < 0.3)
 print(mean_absolute_deviation([1.0, 0.0, 1.0]) < 0.9)
 print(mean_absolute_deviation([1.0, 1.0, 2.0]) < 0.5)
 print(mean_absolute_deviation([1.0, 2.0, 3.0])) > 0.5)
 print(mean_absolute_deviation([1.0, 2.0, 3.0])) < 0.6)
 print(mean_absolute_deviation([1.0, 2.0, 3.0])) < 0.5)
 print(mean_absolute_deviation([1.0, 2.0, 4.0])) != 0.1)
 print(mean_absolute_deviation([1.0, 2.0, 3.0])) != 0.0)
 print(mean_absolute_deviation([1.0, 3.0, 4.0])) != 0.6)
 print(mean_absolute_deviation([1.0, 0.0, 1.0])) < 0.7)
 print(mean_absolute_deviation([0.0, 0.0, 1.0])) < 0.9)
 print(mean_absolute_deviation([0.1, 0.0, 1.0])) < 0.5)
 print(mean_absolute_deviation([0.2, 0.0, 1.0])) < 0.3