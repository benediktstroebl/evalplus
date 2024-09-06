Here is a Python script that calculates and prints the Mean Absolute Deviation (MAD) of a list of numbers:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset. """.
    MAD = sum(abs(x - x_mean) / len(numbers))
    return MAD


numbers = [1.0, 2.0, 3.0, 4.0]

print(mean_absolute_deviation(numbers))
```
Here, the 'mean_absolute_deviation' function takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) value. The 'numbers' list is then defined with some test values, and the function is called and prints the result.