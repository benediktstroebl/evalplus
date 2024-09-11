```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.

    Example:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use built-in functions sum() and prod() to calculate sum and product
    # If the list is empty, the product will be 1 and the sum will be 0 because of the default behavior of these functions
    import math
    return sum(numbers), math.prod(numbers)

# Test the function
print(sum_product([]))  # Should print (0, 1)
print(sum_product([1, 2, 3, 4]))  # Should print (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses the built-in functions `sum` and `math.prod` to calculate the sum and product, respectively. The function returns a tuple containing the sum and product. The script also includes docstrings to provide documentation for the function and examples of how to use it.