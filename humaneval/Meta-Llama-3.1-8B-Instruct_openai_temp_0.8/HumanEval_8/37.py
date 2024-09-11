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
if __name__ == "__main__":
    # Test the function with an empty list
    print(sum_product([]))  # Output: (0, 1)

    # Test the function with a list of numbers
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers and returns a tuple containing the sum and product of all the integers in the list. The function uses a simple iterative approach to calculate the sum and product. The example usage at the end demonstrates how to use the function with both an empty list and a list of numbers.