```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    # Initialize sum to 0 (neutral element for addition) and product to 1 (neutral element for multiplication)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number with the total product
        total_product *= number

    # Return a tuple containing the total sum and total product
    return total_sum, total_product


# Test cases
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
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    # Use the sum function to calculate the total sum
    total_sum = sum(numbers)
    # Use the math.prod function to calculate the total product (default value is 1 for an empty list)
    total_product = math.prod(numbers, start=1)

    # Return a tuple containing the total sum and total product
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```