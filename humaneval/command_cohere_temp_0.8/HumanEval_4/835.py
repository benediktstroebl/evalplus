Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = math.fmean(numbers)
    deviation = sum(math.fabs(x - mean) for x in numbers)
    return deviation / len(numbers)
```
This script defines a function called `mean_absolute_deviation()` that takes in a list of floating numbers and returns the mean absolute deviation of the list. 

The function calculates the mean of the numbers and creates an iterator to calculate the absolute difference between each number and the mean. The iterator is combined into a sum and the number of elements in the list is used to calculate the mean absolute deviation.

This solves the problem and passes the given test case. You can test this script with other input lists to verify its functionality further. Let me know if you need anything else!