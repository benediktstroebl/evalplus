```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and the product of all integers in the list.
    """

    # Initialize sum to 0
    total_sum = 0
    
    # Initialize product to 1
    total_product = 1
    
    # Calculate the sum and product of all numbers in the list
    for num in numbers:
        total_sum += num
        total_product *= num
    
    # Return a tuple containing the sum and product
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, 4)
```