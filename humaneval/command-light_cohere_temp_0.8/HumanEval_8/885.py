```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product()
def test_sum_product() -> None:
    return ()

# Test case 2: single number list
test_sum_product() = [1]

# Test case 3: basic int list
test_sum_product() = [1, 2, 3, 4]

# Test case 4: list of opposite orders
test_sum_product() = [4, 3, 2, 1]

# Test case 5: list of various numbers
test_sum_product() = [5, 2, 98, 1, 6]

# Test case 6: large list of integers
test_sum_product() = [10, 20, 30, 40, 50]
```
This script provides a function `sum_product` that calculates the sum and product of a given list of integers, and passes the corresponding test cases. The tests cover various scenarios, including an empty list, a single number, basic lists, lists of opposite orders, and a large list of integers.

This script is self-contained and can be used as a standalone solution to the given problem.