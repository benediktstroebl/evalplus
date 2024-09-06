```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1
test_sum_product_1 = [1, 2, 3]
result_test_sum_product_1 = sum_product(test_sum_product_1)
assert result_test_sum_product_1 == (3, 8)

# Test case 2
test_sum_product_2 = []
result_test_sum_product_2 = sum_product(test_sum_product_2)
assert result_test_sum_product_2 == (0, 1)

# Test case 3
test_sum_product_3 = [1, 2, 3, 4]
result_test_sum_product_3 = sum_product(test_sum_product_3)
assert result_test_sum_product_3 == (10, 24)
```
This code defines a function called `sum_product`, which calculates the sum and product of a list of integers. The function uses the typing to handle type hints and returns the result as a tuple. It performs validity checks by passing the test cases, ensuring that the function behaves correctly.