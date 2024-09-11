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
    # Initialize sum and product with default values for an empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        
        # Multiply the current number with the product
        # This will work even if the product is 0 (as multiplication by 0 results in 0)
        total_product *= num
    
    # Return the calculated sum and product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of all the integers in a list. The function uses a simple iterative approach to accumulate the sum and product, ensuring that the default values for an empty list (0 for the sum, 1 for the product) are used correctly. The example usage at the end demonstrates how to call this function with both an empty list and a list of numbers.