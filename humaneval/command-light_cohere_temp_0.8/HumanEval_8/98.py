```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    Return values are 0 and 1 are valid inputs for empty and empty product, respectively.
    """
    return (sum(numbers), product(numbers))
    """
    return (sum(numbers), product(numbers)) if len(numbers) > 0 else (0, 1)
```