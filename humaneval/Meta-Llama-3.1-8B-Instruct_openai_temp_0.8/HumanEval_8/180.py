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
    """
    # Calculate the sum of the list. The built-in sum function in Python returns 0 if the list is empty.
    total_sum = sum(numbers)
    
    # Calculate the product of the list. The math.prod function in Python returns 1 if the list is empty.
    import math
    total_product = math.prod(numbers)
    
    # Return a tuple containing the sum and product.
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It uses the built-in `sum` function to calculate the sum and the `math.prod` function from the `math` module to calculate the product. If the input list is empty, the `sum` function returns 0 and the `prod` function returns 1, which is the desired behavior. The example usage at the end demonstrates how to use the `sum_product` function with different inputs.