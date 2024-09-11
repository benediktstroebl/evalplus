```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple where the first element is the sum of all integers in the list, and the second element is the product of all integers in the list.
    """
    
    # Initialize the sum to 0 (the identity for addition) and the product to 1 (the identity for multiplication)
    total_sum = 0
    total_product = 1
    
    # Use the math.prod function to calculate the product of all numbers in the list
    # however math.prod will raise an error for an empty list so we have to handle this edge case
    if numbers:
        total_product = math.prod(numbers)
    
    # Use a list comprehension to sum up all the numbers in the list
    # this will return 0 for an empty list which aligns with the problem description
    total_sum = sum(numbers)
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```