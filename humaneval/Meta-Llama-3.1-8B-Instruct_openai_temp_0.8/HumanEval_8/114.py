```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product()` which takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It initializes `total_sum` to 0 and `total_product` to 1, then iterates over the list of numbers, adding each number to `total_sum` and multiplying each number with `total_product`. Finally, it returns the `total_sum` and `total_product` as a tuple.