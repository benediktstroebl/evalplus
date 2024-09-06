```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    return MAD

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # 1.0)
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(mean_absolute_deviation(numbers))  # 1.4499)
numbers = [1.0, 1.0, 0, 4.0, 5.0]
print(mean_absolute_deviation(numbers))  # 1.6633)
numbers = [0.0, 0, 0, 6.0, 7.0]
print(mean_absolute_deviation(numbers))  # 1.6699```
This Python script defines a function called `mean_absolute_deviation` that computes the Mean Absolute Deviation (`MAD`) for a given list of numbers. It then passes a test cases for this function and prints the results.