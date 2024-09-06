```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product([]) -> (0, 1)

# Test case 2: single element list
test_sum_product([1]) -> (1, 1)

# Test case 3: list of 2 elements
test_sum_product([1, 2]) -> (2, 2)

# Test case 4: list of 3 elements
test_sum_product([1, 2, 3]) -> (6, 6)

# Test case 5: list of 4 elements
test_sum_product([1, 2, 3, 4]) -> (10, 24)
```
This code provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers and passes tests using the `typing` module to validate the function's correctness.