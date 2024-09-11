```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple consisting of the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of all numbers in the list
    product = 1  # Initialize product as 1 to handle empty list
    for num in numbers:  # Iterate over the list to calculate the product
        product *= num
    return total_sum, product  # Return the sum and product as a tuple


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, 4)
```