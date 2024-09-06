```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of integers in a list.

    if not numbers:
        return 0, 1  # Empty sum should be equal to 0, empty product is 1.

    if len(numbers) == 0:
        return 0, 1  # Empty product should be 1

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return product, sum
```