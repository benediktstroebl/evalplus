```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of the integers in the list
    """
    # Initialize sum and product with the base values for empty lists
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
print(sum_product([]))   # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))   # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input, calculates the sum and product of all integers in the list, and returns the result as a tuple. The sum and product are initialized with the base values for empty lists, and then iterated over each number in the list to calculate the sum and product. The function is then tested with the provided test cases.