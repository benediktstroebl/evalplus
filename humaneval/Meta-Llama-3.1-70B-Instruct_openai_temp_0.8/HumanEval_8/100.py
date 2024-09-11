```python
from typing import List, Tuple
import math


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Calculate the sum of all numbers in the list
    total_sum = sum(numbers)
    
    # Calculate the product of all numbers in the list
    # math.prod is available in Python 3.8 and later versions
    # If you are using an earlier version, you can calculate the product using a loop or a recursive function
    if not numbers:
        total_product = 1
    else:
        total_product = math.prod(numbers)
    
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

If you're using a version of Python earlier than 3.8, you can calculate the product without `math.prod` like this:

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Calculate the sum of all numbers in the list
    total_sum = sum(numbers)
    
    # Calculate the product of all numbers in the list
    total_product = 1
    for num in numbers:
        total_product *= num
    
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```