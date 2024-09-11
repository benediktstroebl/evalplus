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
    # Initialize sum and product with default values
    total_sum = 0
    total_product = 1
    
    # Iterate over the input list
    for number in numbers:
        # Add each number to the sum
        total_sum += number
        # Multiply each number with the product
        total_product *= number
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function as specified and includes two test cases to demonstrate its functionality. The function uses a simple iterative approach to calculate the sum and product of the input list.