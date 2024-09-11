```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple where the first element is the sum of the integers in the list and the second element is the product of the integers in the list.
    """
    # Initialize sum and product variables to 0 and 1 respectively
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
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of a given list of integers. It initializes `total_sum` to 0 and `total_product` to 1, then iterates over each number in the list, adding it to `total_sum` and multiplying `total_product` by it. Finally, it returns the sum and product as a tuple. The example usage at the end demonstrates how to use this function with an empty list and a list with integers.