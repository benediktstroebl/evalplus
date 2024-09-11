```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product with the identity values for addition and multiplication
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number with the total product
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can also use the built-in `sum` function for calculating the sum and the `math.prod` function (Python 3.8 and later) or `functools.reduce` for calculating the product:

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
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Calculate the sum using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using the math.prod function (Python 3.8 and later)
    total_product = math.prod(numbers, start=1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Or using `functools.reduce` for product calculation:

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
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Calculate the sum using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using functools.reduce
    total_product = functools.reduce(operator.mul, numbers, 1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))