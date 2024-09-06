Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.fsum(abs(num - sum(numbers) / len(numbers)) for num in numbers) / len(numbers)
```
This Python script defines a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of floats as input and returns the mean absolute deviation as a float. 

The math module is imported to access the `fsum` function for more efficient sum calculation in the loop. The function subtracts the mean from each number in the list, takes the absolute value of each difference, and then calculates the average of those absolute differences using float summation and integer division to preserve decimal points. 

Here's an example of how to use this function:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This would output:
1.0

This value represents the Mean Absolute Deviation (MAD) of the list [1.0, 2.0, 3.0, 4.0], which is 1.0 since all numbers are equally distant from the mean (3.0) and each absolute difference is 1.0.