### Python Script: Sum and Product of Integers in a List

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
    # Use the built-in sum function to calculate the sum of the list
    # If the list is empty, sum will return 0
    total_sum = sum(numbers)
    
    # Use the built-in math.prod function to calculate the product of the list
    # If the list is empty, math.prod will return 1
    # Import the math module
    import math
    total_product = math.prod(numbers)
    
    # Return a tuple containing the sum and product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This Python script defines a function called `sum_product` that takes a list of integers as an argument and returns a tuple containing the sum and product of all the integers in the list. The function uses the built-in `sum` and `math.prod` functions to calculate the sum and product, respectively. The script also includes test cases to verify the function's behavior.