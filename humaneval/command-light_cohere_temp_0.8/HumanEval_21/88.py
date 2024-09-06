```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Initialize the result list with all original numbers
    result = numbers.copy()
    
    # Loop through numbers, multiply each value by the ratio of its size to the largest value
    # Add the rescaled value back to the original list
    for i in range(len(numbers)):
        result[i] = (numbers[i] * (1.0 / float(max_value)))
    return result
``` 
This function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It does this by first initializing a new list with all the original numbers, then multiplying each value in the original list by the ratio of its size to the largest value, and finally adding the rescaled value back to the original list.