```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)  # calculate the sum of the list
    product = 1  # initialize the product variable
    for num in numbers:  # iterate over the list
        product *= num  # multiply each number with the product
    
    return total_sum, product  # return the sum and product as a tuple


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

However, we can also solve this problem using the `math.prod` function for calculating the product of all numbers in the list, which is more Pythonic:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)  # calculate the sum of the list
    product = math.prod(numbers, start=1)  # calculate the product of the list
    
    return total_sum, product  # return the sum and product as a tuple


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```