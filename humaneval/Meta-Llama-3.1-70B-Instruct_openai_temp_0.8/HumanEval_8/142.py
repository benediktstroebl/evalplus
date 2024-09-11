```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple with the sum and product of the integers in the list.
    """
    # Initialize sum and product to the identity elements (0 for sum, 1 for product)
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current number to the product
        total_product *= number
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

Alternatively, you could also use the built-in `sum` and `math.prod` functions in Python to achieve the same result in a more concise way:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple with the sum and product of the integers in the list.
    """
    # Use the sum function to calculate the sum of the numbers
    total_sum = sum(numbers)
    # Use the math.prod function to calculate the product of the numbers
    # math.prod returns 1 for an empty list, which matches the problem requirements
    total_product = math.prod(numbers, start=1)
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```