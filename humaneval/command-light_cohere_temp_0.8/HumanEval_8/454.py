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

# Test case 6: list with large number of elements
test_sum_product([1, 2, 3, 4, 5, 6]) == (16, 120)
```

This Python script presents a function called sum_product, which aims to compute the sum and product of a given list of integers. The function begins by checking whether the input is empty, returning 0 in such cases. It then employs the precise sum and product calculations using the built-in functions sum and product, ensuring accurate results.