```python
from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of all integers in the input list.
    """
    # Calculate the sum of all numbers in the list, defaulting to 0 for empty lists
    total_sum = sum(numbers) if numbers else 0
    
    # Calculate the product of all numbers in the list, defaulting to 1 for empty lists
    # Use reduce with operator.mul to multiply all numbers together
    total_product = reduce(operator.mul, numbers, 1)
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```