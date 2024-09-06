```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    The function accepts a list[float] input and returns the same type.

Test cases:

>>> test_numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0]

>>> rescale_to_unit(test_numbers)
[[0.0, 0.0, 0.0, 0]) # ['0', '1', '2', '3', '4', '5', '6', '7']

>>> test_numbers = [1.0, 1.0, 2.0, 3.0, 4.0, 5, 6, 0, 7]
>>> rescale_to_unit(test_numbers)
[[0.0, 0, 0, 0]) # ['0', '1', '2', '3', '4', '5', '6', '7']

Output: 
```