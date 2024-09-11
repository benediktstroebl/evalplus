### Sum and Product of a List of Numbers

This Python script calculates the sum and product of a given list of integers. If the list is empty, the sum is 0 and the product is 1 by default.

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
    
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        
        # Multiply the current product by the current number
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function uses a simple loop to iterate over each number in the list, updating the sum and product accordingly. The function returns the sum and product as a tuple. The example usage at the end demonstrates how to use the function with empty and non-empty lists.