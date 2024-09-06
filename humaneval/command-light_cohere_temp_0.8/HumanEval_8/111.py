```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:  # empty list
        return (0, 1)
    if len(numbers) == 0:  # empty product
        return (sum(numbers), 0)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)
```