```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of the list of integers."""
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Unit tests
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append((10, 24))
test_sum_product.append((1, 8, 3))
test_sum_product.append((6, 0)) # This should fail

def test_function(test_case: List[int]):
    actual_result = sum_product(test_case)
    assert actual_result == test_case, "Function did not return expected result"

test_sum_product.run(test_function(test_case))
```