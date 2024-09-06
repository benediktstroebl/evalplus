Here's the Python code you requested:
```python
from typing import List, Tuple

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
    assert sum_product([]) == (0, 1)

def test_sum_product_valid():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    assert isinstance(result, Tuple) and len(result) == 2
    assert result == (6, 24)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function then passes the test cases `test_sum_product_empty()` and `test_sum_product_valid()` that check the correctness of the function.