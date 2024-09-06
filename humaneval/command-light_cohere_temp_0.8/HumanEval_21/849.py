```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    : The input is a list of numbers that have at least 2 elements.
    Output is a list of numbers with 0 as the smallest value and 1 as the largest value.
    """
    way of using the numbers as a list (List[num]) in the function, the function first checks if the list has at least two elements. If it has less than two elements, the function raises a ValueError exception. Otherwise, it applies the linear transformation to the list, such that the smallest number will become 0 and the largest will become 1.
    """