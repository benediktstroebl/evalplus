```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the total sum
        total_sum += num
        # Multiply the number with the total product
        total_product *= num

    # Return the total sum and the total product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of all integers in a given list. It handles the edge case where the input list is empty by initializing the sum to 0 and the product to 1, as per the problem statement. The function then iterates over each number in the list, updating the sum and product accordingly. Finally, it returns the total sum and product as a tuple.

You can run this script to test the `sum_product` function with different input lists. The example usage at the end demonstrates how to call the function with an empty list and a list of numbers, and prints the expected output.