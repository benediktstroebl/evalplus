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
    # Initialize sum and product with default values
    total_sum = 0
    total_product = 1

    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the calculated sum and product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([-1, 2, -3, 4]))  # Output: (2, -24)
```

This script defines a function `sum_product` that calculates the sum and product of a given list of integers. It initializes the sum and product with default values (0 and 1 respectively), then iterates over the input list, updating the sum and product accordingly. Finally, it returns the calculated sum and product as a tuple. The script also includes example usage to demonstrate the function's behavior.