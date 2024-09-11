```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the integers in the list.
        Empty sum is equal to 0 and empty product is equal to 1.
    """
    # Initialize sum and product to default values for empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the total product by the current number
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you can use the built-in `sum` function and the `math.prod` function (available in Python 3.8 and later) to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the integers in the list.
        Empty sum is equal to 0 and empty product is equal to 1.
    """
    # Use the sum function to calculate the sum of the numbers
    total_sum = sum(numbers)
    # Use the math.prod function to calculate the product of the numbers
    # If the list is empty, math.prod will return 1
    total_product = math.prod(numbers, start=1)
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```