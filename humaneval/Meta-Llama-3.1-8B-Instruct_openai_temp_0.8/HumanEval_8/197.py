### Python Script
```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Use the built-in sum function to calculate the sum of the numbers in the list
    # The sum function will return 0 if the list is empty, as per the problem statement
    total_sum = sum(numbers)

    # Use the built-in math.prod function to calculate the product of the numbers in the list
    # The math.prod function will return 1 if the list is empty, as per the problem statement
    import math
    total_product = math.prod(numbers)

    # Return a tuple containing the sum and product of the numbers in the list
    return total_sum, total_product


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # Expected output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

### Note:
This script uses the `math.prod` function to calculate the product of the numbers in the list. The `math.prod` function was introduced in Python 3.8 and is not available in earlier versions of Python. If you are using an earlier version of Python, you can use the following alternative implementation:

```python
import functools

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    #...
    total_product = functools.reduce(lambda x, y: x * y, numbers, 1)
    #...
```