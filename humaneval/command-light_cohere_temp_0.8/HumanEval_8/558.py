```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Returns a sum and product as a tuple.

    >>> numbers = [5, 2, 3]
    product = [5 * x for x in numbers] + [10]
    sum = sum(numbers)
    return (sum, product)
    """
    product = [5 * x for x in numbers] + [10]
    sum = sum(numbers)
    return (sum, product)

# Tests
numbers = [5, 2, 3]
result = sum_product(numbers)
print(f"Sum: {result[0]}")
print("Product: ", end="")
for num, pr in result:
    print(f"{num} * {pr} = {num * pr}")

numbers = []
result = sum_product(numbers)
print("\nSum: ", end="")
print("Product: ", end="")
```