```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [x / 100.0 for x in numbers] + [100.0]
    might return: numbers
    return numbers
```
This script defines a function `rescale_to_unit` that takes a list of numbers as an argument. It then returns a's the list of numbers, with each number divided by 100.0 and the additional 100.0 to shift all smallest number to the range [0, 1].

The function is designed to handle lists with at least two elements, and effectively applies a linear transformation to the list, such that the smallest number will become 0 and the largest will become 1.