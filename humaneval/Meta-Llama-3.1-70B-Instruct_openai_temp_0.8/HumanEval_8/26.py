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

    # Initialize sum as 0 and product as 1
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number to the total product
        total_product *= num

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)

# Alternative implementation using built-in functions
def sum_product_alternative(numbers: List[int]) -> Tuple[int, int]:
    """
    Alternative implementation using built-in sum function and math.prod function.
    """
    # Calculate the sum using built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using math.prod function
    # If the list is empty, math.prod will raise a TypeError, so we need to handle this edge case
    total_product = math.prod(numbers) if numbers else 1
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases for alternative implementation
print(sum_product_alternative([]))  # Expected output: (0, 1)
print(sum_product_alternative([1, 2, 3, 4]))  # Expected output: (10, 24)
```