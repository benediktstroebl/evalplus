```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product with default values (0 and 1 respectively)
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add each number to the total sum
        total_sum += num
        # Multiply each number with the total product
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. The function iterates over the list, accumulating the sum and product. It uses default values to handle the edge case where the input list is empty. The script also includes test cases to demonstrate the function's behavior.