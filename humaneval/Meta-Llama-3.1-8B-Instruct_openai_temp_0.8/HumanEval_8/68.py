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
    # Calculate the sum of the integers in the list. By default, sum() function will return 0 for an empty list.
    total_sum = sum(numbers)
    
    # Calculate the product of the integers in the list. By default, math.prod() function will return 1 for an empty list.
    import math
    total_product = math.prod(numbers)
    
    # Return a tuple containing the sum and product of the integers in the list.
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of all integers in a given list. It uses the built-in `sum` function to calculate the sum and the `math.prod` function from the `math` module to calculate the product. The function returns a tuple containing the sum and product. The script also includes test cases to demonstrate the function's behavior.