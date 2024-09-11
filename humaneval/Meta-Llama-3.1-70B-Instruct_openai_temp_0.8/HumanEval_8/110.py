```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    total_sum = sum(numbers)  # Calculate the sum of all numbers in the list
    total_product = 1  # Initialize the product as 1
    for num in numbers:  # Iterate over all numbers in the list
        total_product *= num  # Multiply the current number with the total product
    return total_sum, total_product  # Return the sum and the product as a tuple


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the `math.prod` function (available in Python 3.8 and later) to calculate the product in a more concise way:

```python
import math
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    total_sum = sum(numbers)  # Calculate the sum of all numbers in the list
    total_product = math.prod(numbers, start=1)  # Calculate the product of all numbers in the list
    return total_sum, total_product  # Return the sum and the product as a tuple


# Example usage:
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```