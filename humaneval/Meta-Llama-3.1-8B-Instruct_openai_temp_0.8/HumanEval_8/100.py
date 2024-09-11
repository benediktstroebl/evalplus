```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of all integers in the list.
    """
    # Initialize sum and product with default values for empty list case
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the sum
        total_sum += number
        # Multiply the current product by the current number
        total_product *= number
    
    # Return the calculated sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all integers in the list. It uses a simple iteration to calculate the sum and product, and handles the edge case where the input list is empty. The test cases at the end demonstrate the function's behavior with both an empty list and a non-empty list.