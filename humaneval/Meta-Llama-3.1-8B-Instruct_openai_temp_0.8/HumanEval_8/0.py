### Python Script: Sum and Product of List of Integers
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
    # Initialize sum and product with default values
    total_sum = 0
    total_product = 1

    # Iterate over the input list
    for num in numbers:
        # Add each number to the sum
        total_sum += num
        # Multiply each number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input list. It uses a simple iterative approach to calculate the sum and product. If the input list is empty, it returns the default values (0 for sum and 1 for product). The example usage demonstrates how to call the function with empty and non-empty lists.