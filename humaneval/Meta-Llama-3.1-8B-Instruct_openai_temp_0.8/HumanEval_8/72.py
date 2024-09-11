```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        # Multiply the number with the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with empty list and a list of numbers
print(sum_product([]))
print(sum_product([1, 2, 3, 4]))
```

This script defines the `sum_product` function according to the specification. It initializes the sum and product to 0 and 1 respectively, then iterates over each number in the input list, adding the number to the sum and multiplying it with the product. Finally, it returns a tuple containing the sum and product. The script includes docstrings to provide a clear explanation of the function and its usage, and it includes two test cases to demonstrate the function's behavior.