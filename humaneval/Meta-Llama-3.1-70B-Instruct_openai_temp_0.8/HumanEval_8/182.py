```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum to 0 and product to 1, as per problem statement
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number to the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you could use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to simplify the code:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    return sum(numbers), math.prod(numbers, initial=1)

# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```