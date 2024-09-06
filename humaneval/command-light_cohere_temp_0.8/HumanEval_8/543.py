```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    If the list is empty, return (0, 1)
    If a number in the list is non-negative, return the product of all numbers in the list.
    """
    product = 1
    for num in numbers:
        product *= num
    return product, sum(numbers)
```