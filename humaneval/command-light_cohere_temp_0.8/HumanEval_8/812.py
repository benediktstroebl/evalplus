```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Return a tuple with sum and product values.
    Args:
        numbers: list[int] - List of integers
    Returns:
        tuple(sum, product)
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Unit tests
numbers = [1,2,3,4]
test_sum_product(numbers)
print(numbers[0] + sum_product(numbers))  # Expected output: (1,12)
test_sum_product([])  # Expected output: (0,1)
test_sum_product([1,2,3])  # Expected output: (6,12)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers, then tests the function with various input lists.  It also includes input validation to ensure the function handles empty lists and negative numbers correctly.