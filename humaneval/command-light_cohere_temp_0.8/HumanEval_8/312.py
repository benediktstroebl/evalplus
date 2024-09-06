Here's the self-contained Python function that solves the problem:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a given list of integers.
    >>> sum_product([])
    0
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```
This code defines a function sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. It initializes a sum to 0 and product to 1, then iterates through the list, updating the product and sum accordingly.

This is a self-contained solution to the problem.