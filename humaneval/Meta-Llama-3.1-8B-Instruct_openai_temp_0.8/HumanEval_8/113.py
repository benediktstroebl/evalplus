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

    Example:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum and product with their default values for an empty list
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number with the product
        total_product *= number

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, 1, -1, 1]))  # (0, 1)
print(sum_product([0, 0, 0, 0]))  # (0, 0)
```