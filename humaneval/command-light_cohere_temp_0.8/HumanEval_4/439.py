Here is a self-contained Python script that solves the problem of calculating the mean absolute deviation:
```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation = average | x - x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
   0
   1.0)
   0
   0]  # Use the mean value as the center value
    mad = sum(numbers) / len(numbers)  # Sum of the numbers in the list
    x_mean = mad  # Mean of the numbers in the list
    return abs(x_mean - numbers) ** 2)
```
This function takes a list of numbers as input and returns the Mean Absolute Deviation. It is using the sum of the numbers in the list and the length of the list to calculate the mean, and then it calculates the difference between the mean and the list of numbers and squares that difference.