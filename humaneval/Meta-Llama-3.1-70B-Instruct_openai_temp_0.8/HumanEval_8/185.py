```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and product of the input list.
    """
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the total sum
        total_sum += number
        # Multiply the total product by the number
        total_product *= number
    
    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a list of integers. It uses a simple iterative approach to calculate the sum and product, initializing the sum to 0 and the product to 1 to handle the edge case of an empty list. The function returns a tuple containing the sum and product.

The script also includes two test cases to verify the function's behavior.