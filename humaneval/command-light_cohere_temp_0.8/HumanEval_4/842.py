```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    For a given list of input numbers, calculates the Mean Absolute Deviation 
    around the mean of this dataset.
    MAD = average | x - - x_mean |
    """
    numbers.sort(List(num=len(numbers)//2,asc=True) )
    mean = sum(numbers)/len(numbers)
    absolute_deviation = sum((num - mean) for num in numbers)
    return absolute_deviation
```
This function takes a list of numbers and calculates the Mean Absolute Deviation (MAD) using the formula: 
MAD = average | x - x_mean |

Where: 
- MAD is the Mean Absolute Deviation
- average is the mean of the numbers in the list
- x is each number in the list
- x_mean is the mean of the numbers in the list 

This formula calculates the average absolute difference between each element and the centerpoint (mean) in the list. 
The function then returns the Mean Absolute Deviation value.