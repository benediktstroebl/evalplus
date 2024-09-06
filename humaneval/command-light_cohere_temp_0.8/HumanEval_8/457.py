```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: empty list
test_sum_product("")
assert sum_product([]) == (0, 1)

# Test case 2: single element list
test_sum_product([1])
assert sum_product([1]) == (1, 1)

# Test case 3: double element list
test_sum_product([1, 2])
assert sum_product([1, 2]) == (2, 4)

# Test case 4: triple element list
test_sum_product([1, 2, 3])
assert sum_product([1, 2, 3]) == (6, 6)

# Test case 5: large list
test_sum_product([1, 2, 3, 4, 5])
assert sum_product([1, 2, 3, 4, 5]) == (13, 120)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. It also includes several test cases to verify the correctness of the function. The test cases cover various scenarios, including empty lists, single elements, double elements, and multiple elements.