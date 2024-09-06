```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of the list elements.
    product = 1
    # handle empty list case
    if len(numbers) == 0:
        return (0, 1)
    product = numbers[0]
    for num in numbers[1:]:
        product = num * product
    return (sum(numbers), product)
```