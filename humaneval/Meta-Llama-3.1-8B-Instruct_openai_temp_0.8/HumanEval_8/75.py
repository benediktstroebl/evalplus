```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    # Use the built-in sum function to calculate the sum of the integers
    # If the list is empty, this will return 0
    total_sum = sum(numbers)

    # Use the built-in prod function from the math module to calculate the product of the integers
    # If the list is empty, this will return 1
    import math
    total_product = math.prod(numbers)

    # Return a tuple containing the sum and product
    return total_sum, total_product


# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

Note: The `math.prod` function was introduced in Python 3.8. For earlier versions of Python, you can use the `functools.reduce` function to calculate the product:

```python
import functools
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = sum(numbers)
    total_product = functools.reduce(operator.mul, numbers, 1)
    return total_sum, total_product
```