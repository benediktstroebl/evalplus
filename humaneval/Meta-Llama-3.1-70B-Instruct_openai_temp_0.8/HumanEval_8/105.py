```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    # Calculate the sum of the numbers in the list, using the built-in sum function
    # If the list is empty, sum will return 0
    total_sum = sum(numbers)
    
    # Calculate the product of the numbers in the list, using the math.prod function
    # If the list is empty, math.prod will raise a TypeError, so we return 1 instead
    # We use the math.prod function for Python 3.8 and above, for earlier versions we can use functools.reduce
    import math
    try:
        total_product = math.prod(numbers)
    except TypeError:
        total_product = 1
    
    # Return the sum and the product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```