```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    # Initialize sum and product with neutral elements
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the total sum
        total_sum += number
        # Multiply the number with the total product
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes the sum and product with neutral elements (0 for sum and 1 for product) and then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, it returns the total sum and product as a tuple.

The script also includes test cases to verify that the function works correctly for an empty list and a list of numbers.