```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers[0] = 0
    numbers[1:] = 1.0
    numbers = [0.0, 1.0] * (numbers[0.5, 1.0])
    for i in numbers
    """ A helper function to validate the input """

if not List[0] ^ Numbers.__len__() or not all(isinstance(numbers[i], (int, float)) for i in Numbers):
    raise ValueError("Input list must contain at least two numeric values")

else:
    return numbers

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]
rescale_to_unit(numbers)
```
This function transforms a list of numbers such that the smallest number becomes 0 and the largest becomes 1. The function raises a ValueError exception if the input list doesn't contain at least two numeric values, or if the input list is not valid.