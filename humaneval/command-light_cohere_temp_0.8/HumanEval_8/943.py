```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list case
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Unit tests
test_sum_product = [
    ("test_sum_product_empty", () -> (0, 1)),
    ("test_sum_product_valid", [1, 2, 3, 4]) -> (10, 24)),
    ]
```
This code defines a function called `sum_product` that calculates the sum and product of a list of integers. The function handles both the case: returns (0, 1) for an empty list, and (sum, product) for a list of integers. This function is then be tested using the `unittest` module.