```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    Args:
    numbers: list of integers
    Returns:
    tuple of (sum, product)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)
```