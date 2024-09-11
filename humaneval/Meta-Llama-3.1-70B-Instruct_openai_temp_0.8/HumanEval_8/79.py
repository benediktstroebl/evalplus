```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers: A list of integers.

    Returns:
    A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    product_all = 1
    for num in numbers:
        product_all *= num
    return total_sum, product_all


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
However, the above solution can be optimized by using the `math.prod` function available in Python 3.8 and above, which makes it more concise and Pythonic. Here's the modified version of the function:

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
    A tuple containing the sum and product of the integers in the list.
    """
    return sum(numbers), math.prod(numbers, start=1)


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
This version achieves the same result but with less code and improved readability.