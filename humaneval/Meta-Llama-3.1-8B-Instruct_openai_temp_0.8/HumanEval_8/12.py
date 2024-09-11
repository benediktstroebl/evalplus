```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in a list.
    """
    
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, -2, 3, 4]))  # Expected output: (6, -8)
print(sum_product([10, 0, 5]))  # Expected output: (15, 0)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a simple iterative approach to add up the numbers and multiply them together. The function returns a tuple containing the sum and product. The script also includes some test cases to demonstrate the function's behavior.