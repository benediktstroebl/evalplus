```python
from typing import List

def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.
    MAD = average | x - x_mean |

    Where:
        - x is each input number
        - x_mean is the mean of the list numbers
        - average is the average of x over all the numbers in the list

    Test Case: 
    Input List: [1.0, 2.0, 3.0, 4.0]
    return: 
    >1.7500001104.0
   
    - 1.000 Drean is all functions like the list of numbers in the following format, 
    as a parameter to the mean_absolute_deviation function.
]): 
    Input: [1.0, 2.0, 3.0, 4.0]
   
    return: 
    0.1250000
   
   0
    same for all test cases passed. 
""" 

def average(numbers:
    mean = sum(numbers)/len(numbers)
    return mean

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])) #> 1.75000020