```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    # Initialize sum as 0 and product as 1
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        # Multiply the number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers and returns them as a tuple. The function handles empty lists by initializing the sum to 0 and the product to 1. The script also includes test cases to demonstrate the function's behavior.