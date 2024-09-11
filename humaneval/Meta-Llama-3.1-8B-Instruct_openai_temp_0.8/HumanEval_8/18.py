```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple of sum and product of the given list.
    """
    # Initialize sum and product with neutral elements for list operations
    total_sum = 0
    total_product = 1
    
    # Iterate over the given list of numbers
    for num in numbers:
        # Add current number to the total sum
        total_sum += num
        
        # Multiply current number with the total product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([-1, 2, -3, 4]))  # Output: (2, -24)
```

This Python function `sum_product` calculates the sum and product of a given list of integers using a simple loop. The neutral elements for list operations are used when the list is empty.