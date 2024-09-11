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

    Example:
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = 0  # Initialize sum to 0
    product_of_numbers = 1  # Initialize product to 1

    # Iterate over the input list to calculate the sum and product
    for number in numbers:
        sum_of_numbers += number  # Add each number to the sum
        product_of_numbers *= number  # Multiply each number to the product

    return sum_of_numbers, product_of_numbers  # Return the sum and product as a tuple


# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the input list. The function initializes the sum to 0 and the product to 1, then iterates over the input list to calculate the sum and product. Finally, the function returns the sum and product as a tuple. The script includes example use cases to demonstrate the function's behavior.