Here's a solution to the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    : Return the same list with numbers rescaled
    """
    numbers = [x for x in numbers if x >= 0]
    numbers = [x * (1 + i) for i, x in enumerate((1.0, -1))]
    return numbers
```
This function takes a list of numbers as input and returns a new list with the numbers rescaled. The function first filters out any non-negative values from the input list using the List comprehension. Then, the rescaled list is calculated using a nested list comprehension, where each element is multiplied by (1 + i) to scale it between 0 and 1.

The function then returns the new list with the numbers rescaled.