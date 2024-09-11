```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1

    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script uses Python's built-in `sum` function to calculate the sum of the numbers in the list and the `math.prod` function to calculate the product. Note that `math.prod` was added in Python 3.8, so if you're using an earlier version, you'll need to calculate the product manually, for example with a loop or using the `functools.reduce` function. 

Here's an alternative implementation that works in earlier Python versions:

```python
from typing import List, Tuple
import functools
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = functools.reduce(operator.mul, numbers, 1)

    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```