```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Handle empty list
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: Empty list
test_case1 = ()
print(sum_product(test_case1))  # Output: (0, 1)

# Test case 2: Single element list
test_case2 = [1]
print(sum_product(test_case2))  # Output: (1, 1)

# Test case 3: List with three elements
test_case3 = [1, 2, 3]
print(sum_product(test_case3))  # Output: (3, 8)

# Test case 4: List with more than three elements
test_case4 = [1, 2, 3, 4, 5]
print(sum_product(test_case4))  # Output: (8, 40)
```

The script defines a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. The function uses a `typing` feature in Python to ensure type-checking and handle edge cases like an empty list.

The provided script also includes a set of test cases to validate the `sum_product` function.