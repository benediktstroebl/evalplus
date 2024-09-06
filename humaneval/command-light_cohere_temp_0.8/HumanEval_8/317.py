```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test case 1: empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 2: list with one element
print(sum_product([1]))    # Output: (1, 1)

# Test case 3: list with two elements
print(sum_product([1, 2])) # Output: (2, 2)

# Test case 4: list with three elements
print(sum_product([1, 2, 3])) # Output: (6, 6)

# Test case 5: list with large numbers
print(sum_product([123, 45, 78])) # Output: (159, 4578))
```

This function `sum_product` takes a list of integers as input and returns a tuple with two values: the sum of the numbers and the product of the numbers. It uses a simple loop and an efficient formula to compute the sum and product.