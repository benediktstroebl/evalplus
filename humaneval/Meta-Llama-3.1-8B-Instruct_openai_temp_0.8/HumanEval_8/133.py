```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple of sum and product of the input list.
    """
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        # Multiply the number with the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))   # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script first defines a function `sum_product` that takes a list of integers as input, initializes sum to 0 and product to 1, iterates over each number in the list, adds the number to the sum and multiplies the number with the product, and finally returns the sum and product as a tuple. It then tests the function with an empty list and a list with some numbers.