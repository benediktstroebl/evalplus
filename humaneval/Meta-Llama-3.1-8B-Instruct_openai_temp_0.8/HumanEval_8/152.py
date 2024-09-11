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
    # Initialize sum and product variables to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over the input list of numbers
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number with the product
        total_product *= number

    # Return a tuple containing the sum and product
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a simple iterative approach to accumulate the sum and product, handling the edge cases where the input list is empty. The function returns a tuple containing the sum and product, as required. The example usage demonstrates how to call the function with an empty list and a non-empty list, producing the expected output.