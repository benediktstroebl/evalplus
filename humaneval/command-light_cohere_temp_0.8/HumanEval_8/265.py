```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Tests
test_sum_product_empty()
test_sum_product_valid()

def test_sum_product_empty():
    assert sum_product([]) == (0, 1)

def test_sum_product_valid():
    assert sum_product([1, 2, 3, 4]) == (4, 24)
```

This script defines a function 'sum_product' that calculates the sum and product of a list of integers. The function is then tested using two functions 'test_sum_product_empty' and 'test_sum_product_valid' that verify the function's correctness.