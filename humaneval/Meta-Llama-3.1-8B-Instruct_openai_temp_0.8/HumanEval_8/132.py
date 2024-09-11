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
    # Initialize sum and product with default values for empty lists
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add each number to the sum
        total_sum += num
        # Multiply each number into the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

In this script, we define a function `sum_product` that takes a list of integers as input and returns a tuple of the sum and product of those integers. We use a for loop to iterate over the list, adding each number to the sum and multiplying each number into the product. If the list is empty, the sum is initialized to 0 and the product is initialized to 1.