```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:  # Empty list or tuple
        return (0, 1)
    return (sum(numbers), product(numbers))
    return (sum(numbers), sum(numbers)*product(numbers))
```