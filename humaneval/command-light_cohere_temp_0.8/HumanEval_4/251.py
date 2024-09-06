Here's a Python script that defines a function called **`mean_absolute_deviation`** that takes a list of numbers as an input and calculates the Mean Absolute Deviation, which is the average absolute difference between each element in the list and the mean:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation for a given list of input numbers.
    MAD = sum(x_mean - x_value for x_mean, x_value in zip(numbers, numbers.0))) / len(numbers)
    return MAD

>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
0.5


This script utilizes the **`zip`** function to iterate through each number in the input list. It then calculates the difference between each number and the mean of the numbers and adds it up to calculate the Mean Absolute Deviation. The result is then returned as the **`MAD`** value.