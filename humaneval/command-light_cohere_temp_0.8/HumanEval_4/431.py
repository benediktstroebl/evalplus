```python
from typing import List
import math


def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x - x_mean |
    
    Calculation: 
    For each element in the list: 
    - Calculate the absolute difference between this element and the mean.
    - Sum up absolute differences.
    - Divide the for calculating Mean Absolute Deviation.
    """

def test_mean_absolute_deviation(numbers):
    """
    Test cases for Mean Absolute Deviation
    Function.
    Check if the requires at least 3 numbers.
    Check if the previous test passed and print the result if successful.
    """
   
    print("Passed test cases!") if len(numbers) >= 3 else print("Failed test cases!")

test_mean_absolute_deviation([1.0, 2.0, 3.0])
```