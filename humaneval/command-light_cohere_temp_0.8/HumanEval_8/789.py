```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Args:
    numbers: list[int]
        A list of integers
    Return:
    Tuple[sum, product]
        sum: The sum of the integers in numbers. product the product: 1 and 0
    """
    product = 1
    for num in numbers:
        product = product * num
    sum = sum + num
    return (sum, product)
```