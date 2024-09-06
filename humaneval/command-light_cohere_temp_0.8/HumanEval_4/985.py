```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    Calculate Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [num for num in numbers if type(num) == float]
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    numbers.sort()
   
    mean = sum(numbers)/len(numbers)
    x_mean = mean
    return abs((numbers - x_mean)**2) / (len(numbers) + 1e-1)
```
This code implements a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation for a given list of numbers. The function takes in a list of numbers as input and returns the Mean Absolute Deviation as the output. 
The function first sorts the list of numbers in ascending order. Then, it calculates the mean by summing the numbers and dividing by the length of the numbers. Finally, it calculates the absolute deviation by taking the absolute difference between each number and the mean, then dividing by the length of numbers plus one.