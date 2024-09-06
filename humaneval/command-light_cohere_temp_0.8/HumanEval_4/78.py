Here is a self-contained Python function that calculates and returns the Mean Absolute Deviation of a given list of numbers:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate the mean of this dataset:
    return sum(numbers)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
print_f = [1.0, 2.0, 3.0, 4.0]
print_f = mean(numbers)
print(f"Mean Absolute Deviation: {mean_absolute_deviation(numbers)})")
```

This script defines a function mean_absolute_deviation, which takes a list of numbers and returns the Mean Absolute Deviation. The function also defines another function, mean, which calculates the mean of a given list of numbers. The mean_absolute_deviation function then calls the mean function and returns the result, which is printed out using the print function.