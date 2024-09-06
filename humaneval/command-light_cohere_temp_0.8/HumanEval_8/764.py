```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    >>> numbers = [1, 2, 3, 4]
    return_sum_product([1,2,3,4])
    """
    return_sum_product(numbers)

def return_sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = return_sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)
```