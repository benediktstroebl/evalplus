```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and the product of the input list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    total_sum = sum(numbers)
    product = 1
    for number in numbers:
        product *= number

    # Alternatively, you can use the math.prod function (Python 3.8+)
    # import math
    # product = math.prod(numbers)

    return total_sum, product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
This script defines the `sum_product` function that calculates the sum and product of a list of integers. It uses Python's built-in `sum` function to calculate the sum of the list, and a loop to calculate the product. The function returns a tuple containing the sum and the product.

Note: The script includes a comment about using the `math.prod` function, which is available in Python 3.8 and later. If you're using an earlier version of Python, you can stick with the loop-based implementation.