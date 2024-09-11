```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple consisting of the sum and product of the input list.
    """
    
    # Initialize sum and product to 0 and 1 respectively, as per the problem statement
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num
    
    # Return a tuple consisting of the total sum and total product
    return total_sum, total_product


# Test the function with sample inputs
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([-1, 2, -3, 4]))  # Output: (2, -24)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple consisting of the sum and product of all the integers in the list. It uses a simple iterative approach to calculate the sum and product. The script also includes example use cases to demonstrate the function's behavior.