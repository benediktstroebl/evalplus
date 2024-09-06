Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = math.fmean(numbers)
    deviation = sum(math.fabs(x - mean) for x in numbers)
    return deviation / len(numbers)
```

This function takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. The function calculates the mean of the numbers and then sums up the absolute values of the differences between each number and the mean. The result is divided by the number of elements in the list to get the mean absolute deviation.

To speed up the calculation the `math.fmean` function is used to calculate the mean of the numbers. Since the `math.fabs` function operates on floating point numbers, without loss of generality we assume that the `numbers` list contains floating point numbers as well. 

The script includes corresponding tests in the `test_mean_absolute_deviation.py` file:
```python
def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1, 2, 3, 4]) == 1.0
    assert mean_absolute_deviation([1.5, 2.7, 3.2, 4.9]) == 0.5
    assert mean_absolute_deviation([10, 10, 10, 10]) == 0
    assert mean_absolute_deviation([0, 0, 0, 0]) == 0
```

You can run these tests by copying both files in a Python environment of your choice.