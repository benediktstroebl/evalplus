```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of all integers in the list.
                         Empty sum is equal to 0 and empty product is equal to 1.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script uses the built-in `sum()` function to calculate the sum of all numbers in the list and the `math.prod()` function to calculate the product of all numbers in the list. If the list is empty, `math.prod()` raises a TypeError, so we use a conditional expression to return 1 in that case.

The script also includes the test cases you provided to verify the correctness of the function.