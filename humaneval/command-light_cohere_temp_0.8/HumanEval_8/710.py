```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product_1()
def test_sum_product_1() -> None:
    return
```

The provided code defines a function `sum_product` that calculates the sum and product of a given list of integers. It returns a tested with test cases.

The function first checks if the input list is empty, and if so, returns `(0, 1)` as the result.

If the list is not empty, it uses the built-in functions `sum` and `product` to calculate the sum and product of the numbers in the list.