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
    
    # Use the built-in sum function to calculate the sum of the list. If the list is empty, sum returns 0.
    total_sum = sum(numbers)
    
    # Use the built-in prod function from the math module to calculate the product of the list. If the list is empty, prod returns 1. 
    # We need to import the math module and use prod function for this.
    from math import prod
    total_product = prod(numbers)
    
    # Return a tuple containing the sum and product.
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Note that this script uses the `prod` function from the `math` module to calculate the product of the list. If you are using Python version 3.8 or later, you can use the `math.prod()` function instead. 

Alternatively, if you are using an earlier version of Python, you can calculate the product manually using a loop:

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    total_product = 1
    for num in numbers:
        total_sum += num
        total_product *= num
    return total_sum, total_product
```

This version of the function does not require the `math` module, but it may be less efficient for large lists.