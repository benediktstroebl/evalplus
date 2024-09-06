```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [x/100 for x in numbers]  # Apply a rescaling factor of 0.1/0
   1/ a list
    return numbers
``` 
Do you need help with anything else?