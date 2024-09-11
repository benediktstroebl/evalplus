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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the total product by the number
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a list of integers. The function uses a simple iterative approach to add up the numbers and multiply them together. The script also includes some test cases to verify that the function works correctly.