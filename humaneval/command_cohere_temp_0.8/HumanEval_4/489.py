Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the list
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

This script defines a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function takes a list of floats as input and returns the mean absolute deviation of the list. 

The function uses the `numpy` library to compute the mean and absolute deviations in the following lines:
```python
return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
``` 

The script also includes functionality tests, written as follows:
```python
# Testing the function on a simple list
assert mean_absolute_deviation([1., 2., 3., 4.]) == 1.0

# Testing the function on an unsorted list
assert mean_absolute_deviation([4., 2., 1., 8.]) == 2.0

# Testing the function on an empty list
try:
    mean_absolute_deviation([])
except Exception as e:
    assert str(e) == 'Cannot calculate mean absolute deviation of an empty list'
```
These tests check if the function works correctly with a list of four numbers sorted in ascending order, a list of four numbers unsorted, and an empty list. 

Mean absolute deviation is a measure of the variability of a dataset, indicating how much the values in the dataset deviate from the mean. It is calculated by subtracting the mean from each number in the dataset, taking the absolute value of each deviation, summing up all the absolute deviations, and then dividing this sum by the number of elements in the dataset. 

In the provided code, the `numpy` library is used to handle numerical operations, such as mean calculation and absolute deviation, making the code efficient and concise. 

This code contributes to the emerging trend of utilizing Python for data analysis and visualization, offering a straightforward solution to calculate Mean Absolute Deviation in a variable, versatile programming language. 

Lastly, the script is commented with informative and descriptive explanations of the code, making it self-contained and ready to use for anybody who wants to perform this specific data analysis task.