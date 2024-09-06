```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args:
        numbers: List[int]
    Returns:
        A tuple of (sum, product) where sum is the sum of all integers in the list and product is the product of all integers in the list.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```