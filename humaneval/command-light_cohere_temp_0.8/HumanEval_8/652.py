```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # empty list
        return (0, 1) 
    return (sum(numbers), product(numbers))  # sum product in one line
```