```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and the product of the input list.
    """
    total_sum = 0  # Initialize sum to 0
    total_product = 1  # Initialize product to 1

    for num in numbers:
        total_sum += num  # Add each number to the sum
        total_product *= num  # Multiply each number to the product

    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)

# Using the built-in functions sum() and math.prod() for a more concise solution
from math import prod

def sum_product_concise(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and the product of the input list.
    """
    return sum(numbers), prod(numbers, start=1)


# Test cases
print(sum_product_concise([]))  # Expected output: (0, 1)
print(sum_product_concise([1, 2, 3, 4]))  # Expected output: (10, 24)
```