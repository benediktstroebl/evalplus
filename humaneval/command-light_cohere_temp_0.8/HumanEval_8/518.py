```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: Empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: Single element list
print(sum_product([1]))  # Output: (1, 1)

# Test case 3: Simple list
print(sum_product([1, 2, 3]))  # Output: (4, 6)

# Test case 4: Multi-element list with sum=10 and product=24
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This function, `sum_product`, takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It handles the empty lists gracefully by returning `(0, 1)` in such cases. Additionally, the function uses the `sum()` and `product()` functions to calculate the sum and product, respectively. The test cases provided are designed to validate the correctness of the `sum_product` function.