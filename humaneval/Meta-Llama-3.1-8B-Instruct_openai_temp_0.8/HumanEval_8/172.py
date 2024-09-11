```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Calculate the sum of all integers in the list
    total_sum = sum(numbers)
    
    # Calculate the product of all integers in the list
    # The math.prod function is available in Python 3.8 and later
    # For earlier versions, you can use functools.reduce(lambda x, y: x*y, numbers, 1)
    import math
    total_product = math.prod(numbers)
    
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all integers in the list. It handles the edge case where the input list is empty and uses the `math.prod` function to calculate the product (available in Python 3.8 and later). For earlier versions, you can use the `functools.reduce` function instead. The script also includes docstrings and test cases to demonstrate the function's behavior.