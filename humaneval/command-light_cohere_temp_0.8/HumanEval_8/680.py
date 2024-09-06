```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = [
    'def test_sum_product():
        result = sum_product([1, 2, 3, 4])
        assert result == (4, 24)
    ]
```
This script provides a function sum_product, which calculates the sum and product of a list of integers, and tests the function with an example. The function is designed with type hints to ensure accurate type checking and consistent behavior across different Python versions.