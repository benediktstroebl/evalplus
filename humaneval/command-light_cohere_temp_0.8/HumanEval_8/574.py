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
test_sum_product_single()
test_sum_product_multiple()

def test_sum_product_empty():
    assert sum_product([]) == (0, 1)

def test_sum_product_single():
    assert sum_product([1]) == (1, 1)

def test_sum_product_multiple():
    assert sum_product([1, 2, 3]) == (3, 6)

# Main code
```