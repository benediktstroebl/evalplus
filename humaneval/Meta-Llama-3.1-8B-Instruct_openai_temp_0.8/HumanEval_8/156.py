### Calculating Sum and Product of a List of Numbers
#### A Python Script to Sum and Multiply All Integers in a List

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers, the sum and the product of all numbers in the list.

    Example:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum and product to 0 and 1 respectively, according to problem requirements
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

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script uses a simple for loop to iterate over each number in the list. It initializes `total_sum` to 0 and `total_product` to 1, then adds each number to `total_sum` and multiplies `total_product` by each number. Finally, it returns a tuple containing `total_sum` and `total_product`.