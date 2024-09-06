```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a given list.
    Args: numbers (List[int]): A list of integers.
    Returns: tuple (sum: int, product: int), where sum and product are calculated.
    """
    empty sum should be equal to 0 and empty product should be equal to 1.
    """
    return product"""

# Unit tests
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
assertEqual(result, (5, 120))

numbers = []
result = sum_product(numbers)
assertEqual(result, (0, 1))

numbers = [1, 2, 3, 4]
result = sum_product(numbers)
assertEqual(result, (10, 24))
```

This code defines a function sum_product that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function is then tested using a series of unit tests, which check the validity of the function for different input scenarios.