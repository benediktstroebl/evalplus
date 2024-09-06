```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of all integers in a given list.
    Args:
        numbers: list of integers
    Returns:
        tuple with two elements, the sum and product of all integers in numbers.
    """
    sum = 0
        product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```