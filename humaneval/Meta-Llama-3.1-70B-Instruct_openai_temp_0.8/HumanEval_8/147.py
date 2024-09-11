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
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product variables with default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return a tuple containing the total sum and total product
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)

# Alternative solution using built-in functions
def sum_product_alt(numbers: List[int]) -> Tuple[int, int]:
    """
    Alternative implementation using built-in functions.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Use the built-in sum function to calculate the total sum
    total_sum = sum(numbers)
    # Use the math.prod function (available in Python 3.8+) to calculate the total product
    # If math.prod is not available, you can use functools.reduce with operator.mul
    total_product = math.prod(numbers, initial=1)

    # Return a tuple containing the total sum and total product
    return total_sum, total_product


# Test cases for alternative solution
print(sum_product_alt([]))  # Expected output: (0, 1)
print(sum_product_alt([1, 2, 3, 4]))  # Expected output: (10, 24)
```