Here's the self-contained Python function along with tests for the sum and product of a list of integers:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: Empty list
test_sum_product_empty() -> None
def test_sum_product_empty():
    assert sum_product([]) == (0, 1)

# Test case 2: Single element list
test_sum_product_single() -> None
def test_sum_product_single():
    assert sum_product([1]) == (1, 1)

# Test case 3: Two element list
test_sum_product_two() -> None
def test_sum_product_two():
    assert sum_product([1, 2]) == (2, 4)

# Test case 4: Three element list
test_sum_product_three() -> None
def test_sum_product_three():
    assert sum_product([1, 2, 3]) == (6, 6)

# Test case 5: Four element list
test_sum_product_four() -> None
def test_sum_product_four():
    assert sum_product([1, 2, 3, 4]) == (10, 240)

# Test case 6: Five element list
test_sum_product_five() -> None
def test_sum_product_five():
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function also includes several test cases to validate its behavior. The test cases cover different scenarios, including empty lists, single elements, lists with two and three elements, and lists with four or more elements.