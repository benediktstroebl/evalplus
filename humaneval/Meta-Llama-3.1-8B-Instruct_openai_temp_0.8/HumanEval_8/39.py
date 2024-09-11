```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list
    """
    # Use the built-in functions sum() and prod() from the math module to calculate the sum and product
    from math import prod
    
    # Calculate the sum of the list, using the built-in function sum() which returns 0 for an empty list
    total_sum = sum(numbers)
    
    # Calculate the product of the list, using the built-in function prod() which returns 1 for an empty list
    total_product = prod(numbers)
    
    # Return a tuple containing the sum and product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses the built-in functions `sum()` and `prod()` from the `math` module to calculate the sum and product, respectively. The function returns a tuple containing the sum and product. The script also includes test cases to demonstrate the function's behavior.