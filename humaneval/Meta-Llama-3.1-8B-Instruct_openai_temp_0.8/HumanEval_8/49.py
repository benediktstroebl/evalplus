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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        total_sum += num
        
        # Multiply the number with the product
        product *= num
    
    # Return the sum and product as a tuple
    return total_sum, product

# Test the function
print(sum_product([]))     # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))   # Output: (10, 24)
```

In this script, the `sum_product` function iterates over the input list of numbers, adding each number to the sum and multiplying each number with the product. It initializes the sum and product to 0 and 1 respectively, and returns them as a tuple. The function includes docstrings to provide documentation and example usage.