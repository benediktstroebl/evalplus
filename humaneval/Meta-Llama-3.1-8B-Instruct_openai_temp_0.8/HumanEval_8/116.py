```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple consisting of a sum and a product of all the integers in a list.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize sum and product with 0 and 1 respectively
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

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers, initializes `sum` and `product` to 0 and 1 respectively, then iterates over each number in the list, adding it to `sum` and multiplying it with `product`. Finally, it returns a tuple consisting of `sum` and `product` as required.