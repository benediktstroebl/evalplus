```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple with the sum and product of the input list
    """
    # Initialize sum and product with the default values
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers and returns a tuple with the sum and product of all integers in the list. It uses a for loop to iterate over the list and update the sum and product accordingly. If the input list is empty, it returns (0, 1) by default. The script also includes some test cases to demonstrate the function's behavior.