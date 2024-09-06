Here's the self-contained Python script that solves the problem of scaling down numbers in a given list to a range between 0 and 1, following the function you provided:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # initialize result list
    result = [0.0] * numbers[float]
    
    # create list of minimum and maximum values in the input list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # apply linear transform to all numbers in the input list
    for num in numbers:
        result[0] += (min_val - num) / (max_val - min_val)
        result[1] += (max_val - num) / (max_val - min_val)
    
    # return the result list
    return result
``` 
This function takes a list of numbers as input and returns a new list with the same numbers, but scaled down to a range of 0 to 1. 
The function uses the Pythagorean theorem to scale the numbers in the input list to the desired range. 
By performing the function, the numbers in the input list are multiplied by the difference between the minimum and maximum numbers, divided by the difference between the maximum and minimum numbers, which results in the numbers in the output list being scaled down to the desired range.