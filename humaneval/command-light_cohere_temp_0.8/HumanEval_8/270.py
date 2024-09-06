```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case: empty list
assertEqual(sum_product([]), (0, 1))

# Test case: list with two elements
assertEqual(sum_product([1, 2]), (2, 2))

# Test case: list with three elements
assertEqual(sum_product([1, 2, 3]), (3, 6))

# Test case: list with four elements
assertEqual(sum_product([1, 2, 3, 4]), (4, 24))
```

The provided Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate over the list and accumulate the sum and product. The test cases cover various scenarios, such as an empty list, a list with two elements, a list with three elements, and a list with four elements.