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
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Use math.prod to calculate the product of all numbers in the list
    # math.prod returns 1 for an empty list, which meets the problem's requirements
    product = math.prod(numbers, start=1)
    
    # Use sum function to calculate the sum of all numbers in the list
    # sum returns 0 for an empty list, which meets the problem's requirements
    total = sum(numbers)
    
    return total, product


# Example use cases:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```