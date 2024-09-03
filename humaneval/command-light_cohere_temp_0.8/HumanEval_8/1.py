```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # zero or empty list
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.push([])
test_sum_product.push([1, 2, 3, 4])
test_sum_product.push([5, 6, 7])
test_sum_product.push([10, 20, 30])
test_sum_product.push([21, 42, 60])

def test_function(func:
    func_()
assert func(test_sum_product) == (12, 2)
assert func(test_sum_product[0]) == (6, 1)
assert func(test_sum_product[1]) == (7, 2)
assert func(test_sum_product[2]) == (42, 6)
assert func(test_sum_product[3]) == (60, 12)
assert func(test_sum_product[4]) == (84, 24)
assert func(test_sum_product[5]) == (120, 48)
```