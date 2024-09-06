```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    The function takes a list of numbers and performs a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The rescale_to_unit function uses the list comprehension and the math library to perform the transformation. 

In other words, it scales the numbers so that they are all between 0 and 1, by subtracting the minimum value from the minimum value and dividing the result by the sum of the rest of the numbers.