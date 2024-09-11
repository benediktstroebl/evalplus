```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    :param numbers: A list of integers.
    :return: A tuple containing the sum and product of the input list.
    """
    total_sum = 0
    total_product = 1
    
    for number in numbers:
        total_sum += number
        total_product *= number
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, -4)
print(sum_product([5]))  # Expected output: (5, 5)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to simplify the implementation:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    :param numbers: A list of integers.
    :return: A tuple containing the sum and product of the input list.
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers, initial=1)
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 1, -2, 2]))  # Expected output: (0, -4)
print(sum_product([5]))  # Expected output: (5, 5)
```