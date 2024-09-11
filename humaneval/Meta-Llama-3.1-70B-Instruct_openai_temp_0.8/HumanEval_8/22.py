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
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum to 0 (neutral element for addition) and product to 1 (neutral element for multiplication)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

Alternatively, you can use the built-in `sum()` and `math.prod()` functions in Python to make the code more concise:

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
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Use the sum() function to calculate the sum of the input list
    total_sum = sum(numbers)
    
    # Use the math.prod() function to calculate the product of the input list
    # If the list is empty, math.prod() returns 1 by default
    total_product = math.prod(numbers, start=1)

    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```