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
    
    # Initialize sum and product to 0 and 1, respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the number with the total product
        total_product *= num
    
    # Return a tuple containing the sum and product
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of all integers in a given list. It initializes the sum and product to 0 and 1, respectively, then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, it returns a tuple containing the sum and product.

The script includes docstrings for the function, explaining its purpose, arguments, and return values. It also includes test cases to demonstrate the function's behavior.