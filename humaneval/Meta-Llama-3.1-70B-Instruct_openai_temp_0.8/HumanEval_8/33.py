```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of all integers in the list.
        Empty sum is equal to 0 and empty product is equal to 1.
    """
    
    # Initialize sum and product with their respective neutral elements (0 for sum, 1 for product)
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number with the total product
        total_product *= number
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum()` and `math.prod()` functions (Python 3.8+) to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of all integers in the list.
        Empty sum is equal to 0 and empty product is equal to 1.
    """
    
    # Return the sum and product as a tuple
    return sum(numbers), math.prod(numbers, start=1)


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

In the second version, the `math.prod()` function is used with the `start=1` argument to ensure that an empty product equals 1.