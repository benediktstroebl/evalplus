Here is a Python script that calculates and prints the mean absolute deviation:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    The difference between each element and the mean, is the absolute value of this difference. 
    The absolute value is the most stable way to compare numbers.
    MAD = sum(x - x_mean) / len(numbers)
    return MAD

# Driver code
numbers = [1.0, 2.0, 3.0, 4.0]
print("The mean absolute deviation is: ", mean_absolute_deviation(numbers))
```