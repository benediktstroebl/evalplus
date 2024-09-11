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
    # Use built-in functions to calculate sum and product
    # The sum function takes any iterable and returns the sum of its elements
    # The prod function from the math module takes an iterable and returns the product of its elements
    # We use the math.prod function here as it is available in Python version 3.8 and later
    # If you are using an earlier Python version, you can use functools.reduce instead
    import math
    try:
        # Try to calculate product
        product = math.prod(numbers)
    except ZeroDivisionError:
        # If the list contains zero, the product will be an error
        # In this case, we set the product to 1 as per the problem statement
        product = 1

    # Calculate sum
    total_sum = sum(numbers)

    # Return a tuple with the sum and product
    return total_sum, product


# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses the built-in `sum` function to calculate the sum and the `math.prod` function to calculate the product. The function returns a tuple containing the sum and product. The script also includes a test to demonstrate the function's behavior.