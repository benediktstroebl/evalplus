```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A tuple where the first element is the sum of all integers in the list and the second element is the product of all integers in the list.
    If the list is empty, the function returns (0, 1).
    """
    
    # Initialize sum and product with default values for an empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        
        # Multiply the number with the total product
        total_product *= num
    
    # Return the total sum and the total product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Alternatively, you can use the built-in `sum` function for calculating the sum and the `math.prod` function (available in Python 3.8 and later) for calculating the product, which makes the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A tuple where the first element is the sum of all integers in the list and the second element is the product of all integers in the list.
    If the list is empty, the function returns (0, 1).
    """
    
    # Use the built-in sum function to calculate the sum
    total_sum = sum(numbers)
    
    # Use the math.prod function to calculate the product, defaulting to 1 for an empty list
    total_product = math.prod(numbers, initial=1)
    
    # Return the total sum and the total product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```