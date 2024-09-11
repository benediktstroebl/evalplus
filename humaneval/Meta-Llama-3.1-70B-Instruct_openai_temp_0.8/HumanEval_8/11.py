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
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    
    # Calculate the sum of all the integers in the list
    total_sum = sum(numbers)
    
    # Calculate the product of all the integers in the list using math.prod
    # If the list is empty, math.prod returns 1
    total_product = math.prod(numbers, start=1)
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

However, it is worth noting that `math.prod` is only available in Python 3.8 and later versions. For earlier versions of Python, you can use the following implementation instead:

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
    
    # Calculate the sum of all the integers in the list
    total_sum = sum(numbers)
    
    # Initialize the product to 1
    total_product = 1
    
    # Calculate the product of all the integers in the list
    for num in numbers:
        total_product *= num
    
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```