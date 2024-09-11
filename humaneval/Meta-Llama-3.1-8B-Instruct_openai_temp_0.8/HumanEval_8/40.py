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
    # Initialize sum and product with default values (0 and 1)
    total_sum = 0
    total_product = 1
    
    # Iterate over the input list to calculate sum and product
    for num in numbers:
        total_sum += num
        total_product *= num
    
    # Return the calculated sum and product
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input, calculates the sum and product of all the integers in the list, and returns the results as a tuple. The default values for an empty list (sum = 0, product = 1) are handled within the function itself, ensuring that the function works correctly even when the input list is empty.