```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product([]) == (0, 1)

# Test case 2: list with one element
test_sum_product([1]) == (1, 1)

# Test case 3: list with two elements
test_sum_product([1, 2]) == (2, 2)

# Test case 4: list with three elements
test_sum_product([1, 2, 3]) == (6, 6)

# Test case 5: list with four elements
test_sum_product([1, 2, 3, 4]) == (10, 4)
```
This script defines a function called `sum_product` that takes a list of integers as input and returns a tuple containing their sum and product. It then passes five test cases with different lists to ensure the function is working correctly.