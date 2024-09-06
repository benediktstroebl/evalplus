```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:
        return 0, 1
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return sum, product
```