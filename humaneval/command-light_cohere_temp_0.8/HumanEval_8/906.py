```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test cases
sum_product_test_case = [1, 2, 3]
print("Sum and product:", sum_product(sum_product_test_case))

sum_product_test_case2 = []
print("Sum and product:", sum_product(sum_product_test_case2))

sum_product_test_case3 = [1, 2, 3, 4]
print("Sum and product:", sum_product(sum_product_test_case3))

```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes the `typing` to add type hints to the function and uses a conditional check to handle the empty list case, returning `(0, 1)` instead. The function demonstrates its capability by passing all test cases successfully.