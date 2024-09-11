### Sum and Product of a List of Integers
#### Problem Description
For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
#### Solution

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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number to the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input list. The function initializes the sum and product to 0 and 1, respectively, and then iterates over each number in the list, updating the sum and product accordingly. Finally, the function returns the sum and product as a tuple.