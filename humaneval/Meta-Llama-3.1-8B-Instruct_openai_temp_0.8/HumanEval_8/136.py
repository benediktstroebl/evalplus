### Python Script to Calculate Sum and Product of a List of Numbers
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

    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Initialize sum and product with default values (0 and 1)
    total_sum = 0
    total_product = 1

    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current product by the current number
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product


# Test the function
if __name__ == "__main__":
    print(sum_product([]))  # Output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a given list of numbers. It uses the properties of multiplication to handle the product of an empty list (which should be 1) and the properties of addition to handle the sum of an empty list (which should be 0). The script includes a docstring with examples to demonstrate how to use the function.