```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [x / 100.0 for x in numbers] + [1.0]
    100
   0, 5.0, 4.5]
     numbers = [x / 100.0 for x in numbers]
    return numbers
``` 
This code defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list of numbers with values scaled between 0 and 1, with all other values adjusted accordingly. The code uses the as a list comprehension to create a new list of numbers by dividing each value in the input list by 100 and adding 1. The code then returns the result.