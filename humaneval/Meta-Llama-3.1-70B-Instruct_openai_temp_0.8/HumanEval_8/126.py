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
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over each number in the input list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the total product by the current number
        total_product *= number

    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, -4)
print(sum_product([5]))  # Expected output: (5, 5)
```