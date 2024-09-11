```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and the product of the input list.
    """
    # Initialize sum and product with default values for empty lists
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the total sum
        total_sum += number
        
        # Multiply the total product by the number
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to simplify the code:

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
        A tuple of two integers, the sum and the product of the input list.
    """
    # Use the built-in sum function to calculate the sum
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product
    total_product = math.prod(numbers, start=1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```