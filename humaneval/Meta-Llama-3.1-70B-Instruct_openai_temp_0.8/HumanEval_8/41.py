```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A tuple where the first element is the sum of all integers in the list and the second element is the product of all integers.
    If the list is empty, the function returns (0, 1).
    """
    # Initialize sum to 0 and product to 1 to handle empty list correctly
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This script provides a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function handles empty lists correctly by initializing the sum to 0 and the product to 1. The example usage demonstrates how to use the function with an empty list and a list of integers.