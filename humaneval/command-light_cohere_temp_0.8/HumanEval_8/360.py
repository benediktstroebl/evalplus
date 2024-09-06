```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_sum_product_empty()
test_sum_product_valid()

def test_sum_product_empty():
    assert sum_product([]) == (0, 1)  # Should return (0,1)

def test_sum_product_valid():
    assert sum_product([1, 2, 3, 4]) == (4, 24)  # Should return (4,24)
```

This script defines a `sum_product` function that calculates the sum and product of a list of integers. It also provides test cases to test the correctness of the function. We use type hints and `def` to define the function and test cases separately.