```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of all integers in the list.
    """
    # Initialize sum and product with their respective identity elements
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you could use the built-in `sum` and `math.prod` functions to simplify the code:

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
        A tuple containing the sum and product of all integers in the list.
    """
    # Use the sum function to calculate the sum of the list
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product of the list
    # If the list is empty, math.prod returns 1
    total_product = math.prod(numbers, start=1)

    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```