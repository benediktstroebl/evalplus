```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function calculates the sum and product of all integers in a given list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of all integers in the list.
        If the list is empty, it returns (0, 1).
    """
    
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        
        # Multiply the number to the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

However, a more concise and Pythonic way to solve this problem would be to use the built-in `sum` function for calculating the sum and the `math.prod` function (available in Python 3.8 and later) for calculating the product:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function calculates the sum and product of all integers in a given list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of all integers in the list.
        If the list is empty, it returns (0, 1).
    """
    
    # Use the sum function to calculate the sum of all numbers in the list
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product of all numbers in the list
    # If the list is empty, math.prod will return 1
    total_product = math.prod(numbers, start=1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

If you are using a version of Python earlier than 3.8, you can use the `functools.reduce` function along with the `operator.mul` function to calculate the product:

```python
from typing import List, Tuple
import operator
import functools

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function calculates the sum and product of all integers in a given list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of all integers in the list.
        If the list is empty, it returns (0, 1).
    """
    
    # Use the sum function to calculate the sum of all numbers in the list
    total_sum = sum(numbers)
    
    # Use the functools.reduce function along with operator.mul to calculate the product of all numbers in the list
    # If the list is empty, functools.reduce will raise an error, so we need to handle this case
    total_product = functools.reduce(operator.mul, numbers, 1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum