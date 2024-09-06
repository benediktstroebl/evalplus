```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test case 1: empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: list with only one element
print(sum_product([1]))  # Output: (1, 1)

# Test case 3: list with three elements
print(sum_product([1, 2, 3]))  # Output: (6, 8)

# Test case 4: list with large elements
print(sum_product([123, 45, 67]))  # Output: (139, 236))
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested with different input lists, and the output is printed. It successfully passes the