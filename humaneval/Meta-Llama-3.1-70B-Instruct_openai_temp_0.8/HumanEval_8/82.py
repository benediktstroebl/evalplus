```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input integers
    """

    # Initialize sum and product with default values for empty lists
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number with the product
        total_product *= number

    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (introduced in Python 3.8) to solve this problem in a more concise way:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input integers
    """

    # Use the sum function to calculate the sum and math.prod to calculate the product
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1  # Default product to 1 for empty lists

    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```