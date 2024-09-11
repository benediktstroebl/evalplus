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
    # Initialize sum and product variables to 0 and 1 respectively
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


# Test the function with example inputs
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers and returns a tuple containing the sum and product of all integers in the list. It uses a for loop to iterate over each number in the list, adding it to the sum and multiplying it with the product. The function returns the sum and product as a tuple. The script also includes test cases to demonstrate the function's behavior.