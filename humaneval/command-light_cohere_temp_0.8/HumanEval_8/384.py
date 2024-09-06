```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    Product is the calculated by multiplying each integer by its position, similar to sum().WAYS product:
    product = 1
    for num in numbers:
        product = num * i
    return product + sum(numbers)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result) # Output: (10, 24)
```