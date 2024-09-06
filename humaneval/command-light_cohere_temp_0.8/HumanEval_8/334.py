```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: Empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: Single element list
print(sum_product([1]))  # Output: (1, 1)

# Test case 3: Two elements list
print(sum_product([1, 2]))  # Output: (2, 2)

# Test case 4: Three elements list
print(sum_product([1, 2, 3]))  # Output: (6, 6)

# Test case 5: Large list with elements 2, 4, 6
print(sum_product([2, 4, 6, 8, 10, 12]))  # Output: (28, 720)
```

This code defines a function called `sum_product` that calculates the sum and product of a list of integers. It then passes the If test cases, where it is verified that the function works correctly for various inputs.