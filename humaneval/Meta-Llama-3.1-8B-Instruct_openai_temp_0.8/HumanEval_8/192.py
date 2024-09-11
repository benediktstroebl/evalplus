```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of the sum and product of all the integers in the list.
    """
    # Use the built-in functions sum() and prod() from the math module to calculate the sum and product of the list
    # If the list is empty, the functions will return 0 and 1 respectively
    import math
    sum_result = sum(numbers) if numbers else 0
    product_result = math.prod(numbers) if numbers else 1

    # Return the sum and product as a tuple
    return sum_result, product_result

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a given list of integers. It uses the `sum()` function to calculate the sum and the `math.prod()` function to calculate the product. If the list is empty, the functions return 0 and 1 respectively. The function returns the sum and product as a tuple. The example usage at the end demonstrates how to use this function.