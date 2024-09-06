Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script uses the numpy library to calculate the mean absolute deviation of a list of numbers. 

The function `mean_absolute_deviation` takes a list of numbers as input and returns the mean absolute deviation of the list. The function utilizes numpy's `abs` function to calculate the absolute value of the difference between each element in the list and the mean of the list. The `mean` function then calculates the mean of these absolute differences.

The main logic of the test script is to create a list of test cases containing input lists of floats and the expected output, which is the mean absolute deviation of the input list. 

It loops through each test case, passes the input to the `mean_absolute_deviation` function, and compares the returned value with the expected output. 

To pass the test cases correctly, this script must provide the correct, expected output for the example provided in the problem statement (`[1.0, 2.0, 3.0, 4.0]`) which returns 1.0.

This MAD formula simplifies the process by calculating the distance from the mean rather than the median, offering a straightforward approach to assessing data spread.