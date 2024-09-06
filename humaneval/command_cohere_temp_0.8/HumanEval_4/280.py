Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script uses the numpy library to calculate the mean absolute deviation of a list of numbers. The function `mean_absolute_deviation` takes a list of floats as input and returns the mean absolute deviation of the list. 

The function then creates a numpy array from the list of numbers provided. It then calculates the mean of the array and subtracts it from each number in the array to get the difference from the mean for each value. Then, the absolute value of each of these differences is found, and these are added together before finally taking the mean to arrive at the Mean Absolute Deviation. 

Note: Make sure to install the numpy library before running this script. You can do this by running `pip install numpy`. 
You can test this function by calling it with a list of numbers and comparing the output to the accepted solution above. Here is an example: 
```python
test_list = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(test_list)) 
``` 
This will output: 
```
1.0
``` 

This matches the expected output in the problem statement.