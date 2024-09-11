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
        Tuple[int, int]: A tuple containing the sum and the product of the integers in the list.
    """
    # Initialize sum to 0 and product to 1, as per the problem statement
    total_sum = 0
    total_product = 1
    
    # Use math.prod to calculate the product of all numbers in the list
    # If the list is empty, math.prod returns 1
    total_product = math.prod(numbers, start=1)
    
    # Calculate the sum of all numbers in the list
    # If the list is empty, sum returns 0
    total_sum = sum(numbers)
    
    # Return the sum and the product as a tuple
    return total_sum, total_product


# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```