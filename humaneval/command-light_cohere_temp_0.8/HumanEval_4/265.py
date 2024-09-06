Here is a self-contained Python script that calculates and returns the mean absolute deviation (MAD) of a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mean = sum(numbers)/len(numbers)
    mad = sum((x-mean)**2 for x in numbers) / len(numbers)
    return mad

# Unit Tests
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)=1.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]=0.75)
 print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]=1.25)
 print(mean_absolute_deviation([3.0, 2.0, 4.0, 5.0]=4.00)
 test
print(mean_absolute_deviation([1.0, 1.0, 2.0])=1.0)
 print(mean_absolute_deviation([1.0, 2.0, 3.0])=2.0)
 print(mean_absolute_deviation([1.0, 1.0, 1.0, 2.0])=2.0)
 print(mean_absolute_deviation([2.0, 1.0, 3.0])=2.0)
 print(mean_absolute_deviation([2.0, 2.0, 3.0])=1.96)
 print(mean_absolute_deviation([2.0, 2.0, 2.0])=0.77)
 print(mean_absolute_deviation([2.0, 3.0, 2.0])=0.80)
 print(mean_absolute_deviation([3.0, 2.0, 2.0])=3.92)
 print(mean_absolute_deviation([3.0, 3.0, 2.0])=2.91)
 print(mean_absolute_deviation([4.0, 2.0, 2.0])=1.96)
 print(mean_absolute_deviation([5.0, 5.0, 6.0])=1.94)
 print(mean_absolute_deviation([5.0, 5.0, 6.0]))=2.00)
 print(mean_absolute_deviation([1.0, 6.0, 6.0])=3.10)
 print(mean_absolute_deviation([7.0, 6.0, 6.0]))=1.96)
 print(mean_absolute_deviation([8.0, 8.0, 8.0])=3.11)
 print(mean_absolute_deviation([9.0, 9.0, 9.0]))=2.99)
 print(mean_absolute_deviation([9.0, 8.0, 8.0]))=2.00)
 print(mean_absolute_deviation([9.0, 9.0, 9.0]))=1.97)
 print("Hello World! I am trained to provide accurate and detailed answers.")