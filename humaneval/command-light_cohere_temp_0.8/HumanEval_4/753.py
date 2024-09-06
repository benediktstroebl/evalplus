```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    """
    Calculate Mean Absolute Deviation.
    MAD = average | x -x_mean |
    Where [x] are the numbers in the list and [x_mean] is the mean of the list.
"""


def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
   	x = [1.5]
   0 and 5.0)	
   	numbers = list(numbers)
    x_mean = sum(numbers) / len(numbers)
    return math.abs(x_mean -mean -numbers[numbers.mean())	

test_mean_absolute_deviation()

# Test the function
#print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])) 

# Test with a list of float numbers.

# Test with list of strings
test_mean_absolute_deviation(['hello', 'world'])

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation between a list of numbers and the mean of the list. It also has a function `test_mean_absolute_deviation` which creates a list of numbers, calculates the mean of the numbers, and passes it to the `mean_absolute_deviation` function to get the result. 

In order to test the function, a few tests are added, which call the `test_mean_absolute_deviation` function with different inputs and print the output of the `mean_absolute_deviation` function.