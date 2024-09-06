Here is a self-contained Python function that calculates the Mean Absolute Deviation:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = math.sqrt((sum(x -mean(x) - x_mean) ** 2) / len(numbers)
    return MAD

def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    test_ pass this test the function and output the result.
```
The `mean_absolute_deviation` function computes the Mean Absolute Deviation (MAD) for a list of numbers. The MAD is calculated using the square root of the sum of the squared differences between each element and the mean, divided by the number of elements in the list.