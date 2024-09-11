### Sum and Product of a List of Integers

This Python script defines a function `sum_product` that calculates the sum and product of all integers in a given list.

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
    """
    # Initialize sum and product with the base cases
    total_sum = 0
    total_product = 1

    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the calculated sum and product
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing their sum and product. The base cases for an empty list are handled by initializing the sum to 0 and the product to 1. The function then iterates over the input list, updating the sum and product accordingly. Finally, it returns the calculated sum and product.