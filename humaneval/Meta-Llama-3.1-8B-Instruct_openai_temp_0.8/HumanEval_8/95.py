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
    # Use the built-in functions sum() and prod() from the math module to calculate the sum and product of the list
    # The math.prod() function is available in Python 3.8 and later. For earlier versions, you can use the math.prod() workaround below.
    from math import prod

    # If the list is empty, return (0, 1) as per the problem statement
    if not numbers:
        return 0, 1
    
    # Calculate the sum of the list
    total_sum = sum(numbers)
    
    # Calculate the product of the list
    # For Python 3.8 and later, use the math.prod() function
    # For earlier versions of Python, use the math.prod() workaround below
    if hasattr(prod, '__code__'):  # Check if prod is a function (available in Python 3.8 and later)
        total_product = prod(numbers)
    else:
        # Workaround for math.prod() in earlier versions of Python
        total_product = 1
        for num in numbers:
            total_product *= num
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input integers. The function uses the built-in `sum()` and `math.prod()` functions to calculate the sum and product of the list. The script includes test cases to verify the correctness of the function.