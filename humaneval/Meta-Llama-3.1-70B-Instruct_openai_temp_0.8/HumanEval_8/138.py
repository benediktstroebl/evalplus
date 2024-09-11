```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    total_sum = 0  # Initialize sum to 0
    total_product = 1  # Initialize product to 1

    for num in numbers:
        total_sum += num  # Add each number to the sum
        total_product *= num  # Multiply each number to the product

    return total_sum, total_product  # Return the sum and product as a tuple


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```