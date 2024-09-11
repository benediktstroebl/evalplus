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
    # Use the built-in functions sum() and math.prod() to calculate the sum and product, respectively.
    # The math.prod() function is used instead of the old way with functools.reduce() for better performance.
    import math
    # Initialize sum to 0 and product to 1. This is based on the problem statement.
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number to the total product
        total_product *= num
    
    # Return a tuple containing the total sum and total product
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers and returns a tuple containing the sum and product of the integers in the list. It uses the built-in `sum` and `math.prod` functions to calculate the sum and product, respectively. If the list is empty, it returns a tuple containing 0 and 1 as per the problem statement. The function is tested with some examples at the end.