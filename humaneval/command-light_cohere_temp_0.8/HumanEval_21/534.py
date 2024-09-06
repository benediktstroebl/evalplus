```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    The function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1.

    It returns a the simple, and efficient implementation that only uses the list and its length. 

We first check if the list has at least two elements, if not, we raise an error. If it does, we check if the list has only one element, if so we return that element raised to the power of 0. If the list has more than one elements, we check if the smallest element is equal to 0, if so we return the list as is, otherwise we calculate the new numbers by applying the transformation to each element and then we return the new list.