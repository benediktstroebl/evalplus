```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of all the integers in the list.
    """
    
    # Initialize sum as 0 and product as 1 to handle the case of an empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num
    
    # Return a tuple containing the total sum and the total product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to calculate the sum and product in a more concise way:

```python
import math
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of all the integers in the list.
    """
    
    # Calculate the sum using the built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product using the math.prod function
    total_product = math.prod(numbers, start=1)
    
    # Return a tuple containing the total sum and the total product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```