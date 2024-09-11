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
    # Initialize sum and product with default values
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


# Example usage:
print(sum_product([]))  # Outputs: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Outputs: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a for loop to iterate over each number in the list, accumulating the sum and product through each iteration. Finally, the function returns a tuple containing the calculated sum and product. The example usage at the end demonstrates how to use the function with both an empty list and a list of integers.