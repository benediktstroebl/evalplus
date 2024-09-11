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
    # Use the built-in functions sum() and prod() from the math module to calculate the sum and product
    import math
    # If the list is empty, return (0, 1) as per the problem statement
    if not numbers:
        return 0, 1
    # Calculate the sum and product of the list
    total_sum = sum(numbers)
    total_product = math.prod(numbers)
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script uses the `math.prod()` function to calculate the product of all integers in the list. If the list is empty, it returns (0, 1) as per the problem statement.