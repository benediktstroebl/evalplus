```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of the input list.
    """
    # Initialize sum and product to default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number to the product
        total_product *= number

    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available in Python 3.8+) to simplify the implementation:

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
        A tuple containing the sum and the product of the input list.
    """
    # Calculate sum using built-in sum function
    total_sum = sum(numbers)
    
    # Calculate product using math.prod function (or multiply all numbers manually for Python < 3.8)
    total_product = math.prod(numbers) if numbers else 1

    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```