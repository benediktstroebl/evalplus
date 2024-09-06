```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Numbers that are not numbers or empty sum should return (0, 1)
    """
    if not isinstance(numbers, List) or not all(isinstance(num, int) for num in numbers):
        raise TypeError("Input must be a list of integers")
    if not numbers:
        return (0, 1)
    sum_prod = sum(numbers) *prod(numbers)
    return (sum_prod, sum_prod * prod(numbers))
```