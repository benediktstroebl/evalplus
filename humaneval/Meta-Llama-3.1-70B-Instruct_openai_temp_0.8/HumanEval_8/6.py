```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A tuple of two integers. The first element is the sum of all integers in the list, 
    and the second element is the product of all integers in the list. 
    Empty sum is equal to 0 and empty product is equal to 1.
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as an argument and returns a tuple containing the sum and product of the integers in the list. The `sum` function is used to calculate the sum, and the `math.prod` function (introduced in Python 3.8) is used to calculate the product. If the list is empty, `math.prod` returns 1 by default. 

For versions of Python prior to 3.8, you can calculate the product using a loop:

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    
    return total_sum, total_product
```

Or using the `functools.reduce` function:

```python
import functools
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = sum(numbers)
    total_product = functools.reduce(operator.mul, numbers, 1)
    
    return total_sum, total_product
```