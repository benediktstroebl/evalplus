```python
from typing import List, Tuple
import math
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    
    # Use the built-in sum function to calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product of the numbers
    # If the input list is empty, math.prod returns 1
    total_product = math.prod(numbers, start=1)
    
    # Alternatively, you can use the functools.reduce function with the operator.mul function
    # to calculate the product of the numbers
    # total_product = functools.reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```