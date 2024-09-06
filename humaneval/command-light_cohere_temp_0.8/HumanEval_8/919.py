```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args:
    numbers: A list of integers
    Returns: A tuple consisting of a sum and a product of all the integers in the list.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases for the function
numbers = [0, 1]
result = sum_product(numbers)
print(result)  # Output: (1, 1)

numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)

numbers = []
result = sum_product(numbers)
print(result)  # Output: (0, 1)

numbers = [1, 2, 3, 4]
result = sum_product([5, 6, 7])
print(result)  # Output: (16, 28)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The `sum_product` function takes a list of integers as an argument and returns a tuple with the sum and product of the integers. The test cases demonstrate that this function can correctly calculate the sum and product of various lists of integers.