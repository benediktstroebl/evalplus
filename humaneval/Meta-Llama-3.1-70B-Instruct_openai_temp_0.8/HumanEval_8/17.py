```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    total_sum = 0
    product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the total sum
        total_sum += number
        # Multiply the product by the number
        product *= number
    
    # Return the sum and product as a tuple
    return total_sum, product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
Alternatively, you can use built-in Python functions `sum` and `math.prod` to solve this problem in a more concise way:

```python
import math
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    product = math.prod(numbers, start=1)
    
    # Return the sum and product as a tuple
    return total_sum, product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```