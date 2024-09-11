```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input integers.
    """

    # Initialize sum and product to their respective identities (0 for sum, 1 for product)
    total_sum = 0
    total_product = 1

    # Iterate over the input list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the total product by the current number
        total_product *= num

    # Return a tuple containing the total sum and the total product
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing their sum and product. The function initializes the sum to 0 and the product to 1, then iterates over the input list, updating the sum and product accordingly. Finally, it returns a tuple containing the total sum and the total product. The example usage demonstrates the function's behavior with an empty list and a list of integers.