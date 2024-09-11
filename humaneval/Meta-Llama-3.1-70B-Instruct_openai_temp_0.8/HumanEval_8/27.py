```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        # Multiply the product by the number
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function initializes the sum to 0 and the product to 1, then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, the function returns the sum and product as a tuple.

The script also includes two test cases to demonstrate the function's behavior.