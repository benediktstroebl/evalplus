```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    # Initialize sum to 0 (neutral element for addition) and product to 1 (neutral element for multiplication)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the total product by the current number
        total_product *= number

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

You can also solve this problem using built-in `sum` function in Python, which makes the code more concise:

```python
from typing import List, Tuple
from math import prod

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    # Use built-in sum function to calculate the sum
    total_sum = sum(numbers)
    # Use math.prod function (Python 3.8+) to calculate the product
    # For earlier versions, use functools.reduce operator or a loop
    total_product = prod(numbers, start=1)

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

If you are using an earlier version of Python that does not support `math.prod`, you can use `functools.reduce` instead:

```python
from typing import List, Tuple
import functools
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    # Use built-in sum function to calculate the sum
    total_sum = sum(numbers)
    # Use functools.reduce to calculate the product
    total_product = functools.reduce(operator.mul, numbers, 1)

    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 