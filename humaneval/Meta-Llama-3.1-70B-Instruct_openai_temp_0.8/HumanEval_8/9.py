```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product with default values for an empty list
    total_sum = 0
    total_product = 1

    # Iterate over the numbers in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can also use the built-in `sum` function for calculating the sum and the `math.prod` function (Python 3.8+) for calculating the product:

```python
import math
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    # Calculate the sum using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using the math.prod function (Python 3.8+)
    total_product = math.prod(numbers, start=1)

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This alternative solution is more concise but requires Python 3.8 or later due to the use of `math.prod`.