```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
This function takes a list of numbers and returns a new list with the numbers rescaled so that they are all between 0 and 1. The function uses the list comprehension and the division by 100.