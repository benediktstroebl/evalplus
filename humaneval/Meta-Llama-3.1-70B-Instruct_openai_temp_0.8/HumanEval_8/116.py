```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    
    # Initialize sum to 0 (neutral element for addition)
    total_sum = 0
    
    # Initialize product to 1 (neutral element for multiplication)
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        
        # Multiply the number to the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)

# Alternative implementation using built-in functions
def sum_product_alternative(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    
    # Calculate the sum using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using the math.prod function (Python 3.8+)
    # If you're using an earlier version of Python, you can use the functools.reduce function instead
    total_product = math.prod(numbers, start=1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product_alternative([]))  # Expected output: (0, 1)
print(sum_product_alternative([1, 2, 3, 4]))  # Expected output: (10, 24)
```