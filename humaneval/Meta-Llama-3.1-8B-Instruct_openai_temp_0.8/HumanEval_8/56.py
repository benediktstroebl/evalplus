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
    # Use the built-in sum function to calculate the sum of the list
    # If the list is empty, sum returns 0
    total_sum = sum(numbers)
    
    # Use the built-in prod function from the math module to calculate the product of the list
    # If the list is empty, prod returns 1
    from math import prod
    total_product = prod(numbers)
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script first defines the `sum_product` function, which uses the built-in `sum` and `prod` functions from the `math` module to calculate the sum and product of the input list. The function then returns these values as a tuple. Finally, the script tests the function with the provided examples.