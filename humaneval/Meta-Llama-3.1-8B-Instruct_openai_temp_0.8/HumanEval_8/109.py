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
    # Initialize sum and product with the default values
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # For each number, add it to the sum and multiply it with the product
        total_sum += num
        total_product *= num
        
    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of these integers. The example usage at the end demonstrates how to use this function with both an empty list and a list containing integers.