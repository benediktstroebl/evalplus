### Sum and Product of a List of Integers
#### Python Solution
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add each number to the sum
        total_sum += num
        # Multiply each number to the product
        product *= num
    
    # Return the sum and product as a tuple
    return total_sum, product

# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It iterates over the list, adding each number to the sum and multiplying each number to the product. If the list is empty, the sum is initialized to 0 and the product is initialized to 1. The function returns a tuple containing the sum and product. The example usage demonstrates how to call the function with an empty list and a list of integers.