```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input integers.
    """
    
    # Check if the list is empty
    if not numbers:
        # Return default values for empty sum (0) and empty product (1)
        return 0, 1
    
    # Use initial values for sum and product
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input. It uses a for loop to calculate the sum and product of all the numbers in the list. If the input list is empty, it returns default values for sum (0) and product (1). The function is then tested with some examples to demonstrate its usage.