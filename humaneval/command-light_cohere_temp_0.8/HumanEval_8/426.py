```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    if not numbers:  # Empty list
        return (0, 1)
    # Calculate sum
    sum = sum(numbers)
    # Calculate product
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)
```