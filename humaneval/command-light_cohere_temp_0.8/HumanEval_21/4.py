```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [num / min(numbers) for num in numbers]
    return [x / min(numbers) for x in numbers]

# Test
# [rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
return [0.0, 0.0, 0.0, 0.0]
#
# print the result of the function with the above test 

# print(rescale_to_unit([1.0, 2.0, 3.0, 4]))
# 
``` 
The function uses the List comprehension technique to calculate the new numbers. 

The result is then returned.