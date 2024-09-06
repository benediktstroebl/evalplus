```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Input: numbers: List[float]
    """
    numbers[0] = 0  # Set the smallest number to 0
    numbers[1] = 1  # Set the largest number to 1
    return numbers
```
This code defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list with the numbers rescaled to have their smallest value become 0 and their largest value become 1. The function achieves this by assigning the smallest number to 0 and the largest number to 1.