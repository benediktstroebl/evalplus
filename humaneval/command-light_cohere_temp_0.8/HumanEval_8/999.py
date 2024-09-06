```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:
        return 0, 1
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return product, sum
```