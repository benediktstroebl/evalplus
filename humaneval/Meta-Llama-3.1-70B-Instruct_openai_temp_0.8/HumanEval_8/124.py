```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the input list.
    """
    # Initialize sum to 0 and product to 1, as specified in the problem
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the number to the total product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you could use the built-in `sum` and `math.prod` functions to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the input list.
    """
    # Use sum function to calculate the sum of the list
    total_sum = sum(numbers)
    
    # Use math.prod function to calculate the product of the list
    # If the list is empty, math.prod will raise a TypeError, so we need to handle this case
    total_product = math.prod(numbers) if numbers else 1
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```