```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input integers.
    """
    total_sum = 0  # Initialize sum as 0
    total_product = 1  # Initialize product as 1

    for num in numbers:
        total_sum += num  # Add each number to the total sum
        total_product *= num  # Multiply each number to the total product

    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum()` function and the `math.prod()` function (available in Python 3.8+) to simplify the code:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input integers.
    """
    total_sum = sum(numbers)  # Calculate sum using built-in sum function
    total_product = math.prod(numbers)  # Calculate product using math.prod function

    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```