```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of all the integers in the list.
    """
    # Use the built-in sum function to calculate the sum of the list
    total_sum = sum(numbers)
    
    # Use the math.prod function (Python 3.8+) to calculate the product of the list
    # If the list is empty, math.prod will return 1
    total_product = math.prod(numbers, start=1)
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Note: If you're using a version of Python prior to 3.8, you won't have access to the `math.prod` function. In that case, you can use the following alternative implementation for the `sum_product` function:

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of all the integers in the list.
    """
    # Use the built-in sum function to calculate the sum of the list
    total_sum = sum(numbers)
    
    # Initialize the total product to 1
    total_product = 1
    
    # Calculate the product of the list
    for num in numbers:
        total_product *= num
    
    return total_sum, total_product
```