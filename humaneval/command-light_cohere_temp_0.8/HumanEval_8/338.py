```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
assert isinstance(result, Tuple)
assert len(result) == 2
assert result[0] == numbers[0] + sum_of_products(numbers)
assert result[1] == numbers[0] * product

numbers = []
result = sum_product(numbers)
assert result == (0, 1)

def sum_of_products(numbers: List[int]) -> int:
    sum = 0
    for num in numbers:
        sum += num
    return sum
```