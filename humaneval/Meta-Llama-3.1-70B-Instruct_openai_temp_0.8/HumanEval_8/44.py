```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple consisting of a sum and a product of all the integers in a list.
    """
    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total_sum, product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the `math.prod` function (available in Python 3.8+) to calculate the product of all numbers in the list:

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
        A tuple consisting of a sum and a product of all the integers in a list.
    """
    total_sum = sum(numbers)
    product = math.prod(numbers, start=1)
    return total_sum, product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Note: In the `math.prod` version, we use the `start=1` parameter to specify that the product of an empty list should be 1.