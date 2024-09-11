```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple consisting of the sum and product of all integers in the list.
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
print(sum_product([]))   # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This Python script defines a function `sum_product` that calculates the sum and product of all integers in a given list. It initializes the sum and product with 0 and 1 respectively, then iterates over each number in the list, updating the sum and product accordingly. The function returns a tuple consisting of the sum and product. The example usage demonstrates the function's behavior with an empty list and a non-empty list.