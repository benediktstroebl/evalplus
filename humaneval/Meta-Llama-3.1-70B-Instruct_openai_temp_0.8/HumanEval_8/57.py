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

    # Initialize sum and product with default values for empty list
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


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Alternatively, you can use Python's built-in `sum()` function and the `math.prod()` function (introduced in Python 3.8) to simplify the implementation:

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

    # Use sum() function to calculate the sum of the list
    total_sum = sum(numbers)
    
    # Use math.prod() function to calculate the product of the list
    # If the list is empty, math.prod() returns 1 by default
    total_product = math.prod(numbers, start=1)

    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

For Python versions before 3.8, you can define a custom `prod` function using the `functools.reduce` function:

```python
from typing import List, Tuple
import functools
import operator

def prod(numbers: List[int]) -> int:
    """
    Calculate the product of a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The product of the input list.
    """

    # Use functools.reduce() to calculate the product of the list
    # If the list is empty, functools.reduce() raises a TypeError
    # So, we use a default value of 1 to handle the empty list case
    return functools.reduce(operator.mul, numbers, 1)


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the