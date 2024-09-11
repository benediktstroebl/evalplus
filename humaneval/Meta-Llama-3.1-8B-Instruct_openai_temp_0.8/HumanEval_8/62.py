```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Initialize sum and product with the first element of the list
    total_sum = numbers[0]
    total_product = numbers[0]
    
    # Iterate over the rest of the list
    for num in numbers[1:]:
        # Add each number to the sum
        total_sum += num
        # Multiply each number to the product
        total_product *= num
    
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Alternatively, you can also use the built-in functions `sum` and `math.prod` to make the code more concise:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    # Handle the edge case where the list is empty
    if not numbers:
        return 0, 1
    
    # Use built-in functions to calculate sum and product
    return sum(numbers), math.prod(numbers)

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```