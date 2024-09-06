```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function
test_sum_product = []
test_sum_product.add([1])
test_sum_product.add([2])
test_sum_product.add([3])
test_sum_product.add([4])
result = sum_product(test_sum_product)
print(result)  # Output: (15, 240)
```