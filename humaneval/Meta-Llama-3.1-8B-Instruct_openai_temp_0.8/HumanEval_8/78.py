```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers

    Returns:
        A tuple of two integers: the sum and the product of all the integers in the list
    """
    # Initialize the sum to 0 and the product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        # Multiply the number with the product
        total_product *= num
        
    # Return the sum and the product as a tuple
    return total_sum, total_product


# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This Python script defines a function `sum_product` that takes a list of integers as input, calculates the sum and product of all the integers in the list, and returns the results as a tuple. The function handles the case where the input list is empty by initializing the sum to 0 and the product to 1. The script also includes two test cases at the end to verify that the function works correctly.