```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function uses a for loop to iterate over the list, adding each number to the sum and multiplying each number with the product. The function finally returns the sum and product as a tuple. The script also includes test cases to demonstrate the function's behavior.