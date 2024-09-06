```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    The function takes in a list of numbers as a parameter and returns a new list with the applied linear transformation.
    
    It first checks if the f the list has at least two elements, if not, the function returns the list as it is.
    """