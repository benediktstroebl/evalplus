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
    # Initialize sum and product with default values
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the product by the current number
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script uses a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input list. The function initializes the sum and product with default values of 0 and 1, respectively, and then iterates over the input list, updating the sum and product accordingly. Finally, the function returns the sum and product as a tuple. The script includes example usage of the function.