```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with an empty list
test_sum_product() {
    assert sum_product([]) == (0, 1)
}

# Test the function with list of integers
test_sum_product() {
    assert sum_product([1, 2, 3, 4]) == (10, 24)
}
```
This Python script provides a self-contained function `sum_product` that calculates the sum and product of a list of integers. It also includes unit tests to verify the correctness of the `sum_product` function with both empty and non-empty lists.  This test a test it with an empty list and a list of integers to ensure that the function behaves as expected.