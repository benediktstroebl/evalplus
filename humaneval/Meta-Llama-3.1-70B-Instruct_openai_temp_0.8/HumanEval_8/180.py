```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, where the first element is the sum of all integers in the list and the second element is the product of all integers in the list.
    """
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1

    # Calculate sum and product of all numbers in the list
    for num in numbers:
        total_sum += num
        total_product *= num

    # Return sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 0, 1]))  # Expected output: (0, 0)
print(sum_product([5]))  # Expected output: (5, 5)
```

This script defines the `sum_product` function that calculates the sum and product of all integers in a given list. It handles the edge case where the input list is empty by initializing the sum and product with default values (0 and 1, respectively). The function then iterates over the list, updating the sum and product accordingly. Finally, it returns the calculated sum and product as a tuple.

The script also includes test cases to demonstrate the function's correctness.