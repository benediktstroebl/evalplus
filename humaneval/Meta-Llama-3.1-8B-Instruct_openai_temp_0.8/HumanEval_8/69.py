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
    # Use the built-in sum function to calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Initialize the product to 1
    total_product = 1
    
    # Use a for loop to multiply each number in the list to the product
    for num in numbers:
        total_product *= num
    
    # Return a tuple consisting of the sum and the product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple consisting of the sum and product of all the integers in the list. The function uses the built-in `sum` function to calculate the sum and a for loop to calculate the product. The script also includes some test cases to demonstrate the function's behavior.