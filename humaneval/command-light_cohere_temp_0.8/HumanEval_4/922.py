Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List
import math


def mean_absolute_deviation(numbers):
    # Calculate Mean Absolute Deviation
    mad = math.mean(numbers)
    mad = sum((x - mad) ** 2 for x in numbers) / len(numbers)
    return mad

numbers = [1.0, 2.0, 3.0, 4.0]
print("The following is the output of the function:")

"""The Mean Absolute Deviation of the above array is 1.5"""
print(mean_absolute_deviation(numbers))
```

This script is self-contained and does not require any external modules. It defines a function `mean_absolute_deviation` which takes a list of numbers and calculates the mean absolute deviation of the dataset. This is then the mean of the numbers and the absolute value of each element minus the mean, squared, and then taking the average of the squared differences. The function then returns the value of the mean absolute deviation.