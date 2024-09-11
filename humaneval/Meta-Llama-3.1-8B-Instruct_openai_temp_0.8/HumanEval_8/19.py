```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    sum_of_numbers = 0  # Initialize sum as 0
    product_of_numbers = 1  # Initialize product as 1

    # Iterate over each number in the list
    for number in numbers:
        sum_of_numbers += number  # Add the number to the sum
        product_of_numbers *= number  # Multiply the product by the number

    return sum_of_numbers, product_of_numbers  # Return the sum and product as a tuple


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers, following the specified rules. The function is well-documented with a docstring, and an example usage is provided at the end to demonstrate how to use the function.