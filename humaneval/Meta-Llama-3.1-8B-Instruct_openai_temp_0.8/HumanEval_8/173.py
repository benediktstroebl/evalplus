```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list.

    Examples:
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Use the built-in functions sum() and math.prod() to calculate the sum and product of the list
    # The math.prod function was added in Python 3.8, for earlier versions use functools.reduce instead
    from math import prod
    if not numbers:  # Check if the list is empty
        return 0, 1
    else:
        # Calculate the sum and product of the list
        sum_of_numbers = sum(numbers)
        product_of_numbers = prod(numbers)
        return sum_of_numbers, product_of_numbers

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, -2, -3, -4]))  # (-10, -24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function uses the built-in `sum` and `math.prod` functions to calculate the sum and product, and handles the case where the list is empty by returning (0, 1). The script also includes test cases to demonstrate the function's behavior.