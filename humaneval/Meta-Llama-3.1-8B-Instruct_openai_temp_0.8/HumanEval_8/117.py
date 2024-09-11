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
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Calculate the sum of the list using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product of the list by multiplying all numbers together
    total_product = 1
    for num in numbers:
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It handles the edge case where the input list is empty by returning (0, 1). The sum is calculated using the built-in `sum` function, and the product is calculated by multiplying all numbers together using a for loop. The function is then tested with the provided examples.