```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # empty list
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```