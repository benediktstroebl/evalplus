```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various inputs
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append([5, 6, 9])
test_sum_product.append([10, 20])
test_sum_product.append([21, 100])

# Print the result
print("Sum:", sum_product(test_sum_product))
print("Product:", sum_product(test_sum_product))
```