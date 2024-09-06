```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
This Python script defines a function rescale_to_unit that takes a list of numbers and applies a linear transformation to the list, such that the smallest number becomes 0 and the largest becomes 1. The function first creates a list of numbers, then applies the transformation to it and returns the new list. This function can be useful in various situations where you need to perform a linear transformation on a list of numbers.