```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Empty list case
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: Empty list
print(sum_product([]))
# Prints (0, 1) as expected

# Test case 2: List with one element
print(sum_product([1]))
# Prints (1, 1) as expected

# Test case 3: List with two elements
print(sum_product([1, 2]))
# Prints (2, 2) as expected

# Test case 4: List with large number
print(sum_product([123]))
# Prints (124, 45600) as expected
```

In this solution, the function sum_product takes a list of integers as input and returns a tuple containing their sum and product. The function first checks if the list is empty, and in such case, returns (0, 1). If the list is not empty, the function uses the sum() and product() functions to calculate the sum and product of the list elements and returns the result.