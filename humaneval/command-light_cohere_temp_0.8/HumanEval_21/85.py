```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    numbers = [x / (min(numbers) - max(numbers))
    return [x / (x - max(numbers)) for x in numbers]
```
This script defines a function called rescale_to_unit that takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number in the list will become 0 and the largest number will become 1. 
The function uses the list comprehension and the min and max functions to calculate the minimum and maximum values in the list, and then scales the list such that the smallest value becomes 0. 
The function then returns a new list with the rescaled values.