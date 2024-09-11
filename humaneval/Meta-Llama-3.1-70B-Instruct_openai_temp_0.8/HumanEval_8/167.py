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

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, 4)
```

This script defines the `sum_product` function, which initializes `total_sum` to 0 and `total_product` to 1. It then iterates over the input list, adding each number to `total_sum` and multiplying each number with `total_product`. Finally, it returns the calculated sum and product as a tuple.

The script also includes test cases to verify the function's behavior with different inputs.