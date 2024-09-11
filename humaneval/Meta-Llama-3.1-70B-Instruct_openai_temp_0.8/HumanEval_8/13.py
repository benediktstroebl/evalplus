```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the input list.
    """
    # Use built-in sum function to calculate the sum of the list, defaulting to 0 if the list is empty
    total_sum = sum(numbers)
    
    # Use math.prod function to calculate the product of the list, defaulting to 1 if the list is empty
    # math.prod is available in Python 3.8 and later, for earlier versions use functools.reduce
    total_product = math.prod(numbers, start=1)
    
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

If you're using a version of Python earlier than 3.8, you can use the `functools.reduce` function to calculate the product:

```python
import functools
import operator
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the input list.
    """
    total_sum = sum(numbers)
    total_product = functools.reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```