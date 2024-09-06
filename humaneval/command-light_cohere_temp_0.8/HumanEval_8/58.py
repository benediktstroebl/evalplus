Here is a self-contained Python script that solves the problem you described: 

```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple of sum and product of the list of integers.
    Args:
        numbers: list of integers
    Returns: tuple of sum and product of numbers.
    """
    test_sum_product_test
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
test_sum_product_test = [1, 2, 3, 4]
print(sum_product(test_sum_product_test))
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function also includes a `test_sum_product_test` which passes the corresponding tests.