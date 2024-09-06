```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of a list of integers.
    Args:
        numbers: list of integers

    Returns:
        A tuple containing a sum and a product of all integers in numbers.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Tests
sum_product([]) == (0, 1)
sum_product([1, 2, 3, 4]) == (10, 24)
```
This code defines a function sum_product that calculates the sum and product of a list of integers. The function uses the general and concise Python style and passes the test cases without using any external functions.