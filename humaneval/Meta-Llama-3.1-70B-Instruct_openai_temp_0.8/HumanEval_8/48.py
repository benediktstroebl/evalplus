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
    """
    total_sum = 0
    total_product = 1
    
    for number in numbers:
        total_sum += number
        total_product *= number
    
    return total_sum, total_product


# Example use cases:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

However, this can also be achieved in a more Pythonic way using built-in functions:

```python
from typing import List, Tuple
import math
import functools
import operator


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1
    
    return total_sum, total_product


# For older Python versions (before 3.8), math.prod() is not available, 
# so we can use functools.reduce() instead:

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = functools.reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product


# Example use cases:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```