Here is a Python script that contains a self-contained function with proper docstrings and comments to pass the test cases:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
    numbers: List[int] - List of integers

    Returns:
    tuple - A tuple consisting of a sum and a product of all the integers in the list.
    """
    numbers = sorted(numbers)  # Sort the list to ensure a stable product calculation
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Test cases
test_sum_product = [1, 2, 3, 4]
test_sum_product_empty = []
test_sum_product_large = [123, 456, 789, 0]

results = sum_product(test_sum_product)
assert results == (6, 24)

results2 = sum_product(test_sum_product_empty)
assert results2 == (0, 1)

results3 = sum_product(test_sum_product_large)
assert results3 == (310, 3562007940)
```
This script defines a function `sum_product` that calculates the sum and product of a given list of integers. It also provides test cases with various input lists to test the correctness of the function. The function is designed with proper docstrings and comments to explain its purpose and functionality.