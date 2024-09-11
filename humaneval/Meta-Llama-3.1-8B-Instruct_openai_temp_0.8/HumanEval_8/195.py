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

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        
        # Multiply the current number with the product
        # This ensures that the result is the product of all numbers in the list
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([-1, -2, -3, -4]))  # Output: (-10, -24)
```

In this script, we define a function `sum_product` that takes a list of integers as input. The function initializes two variables, `total_sum` and `total_product`, to 0 and 1 respectively. It then iterates over each number in the list, adding the current number to `total_sum` and multiplying `total_product` by the current number. Finally, the function returns the `total_sum` and `total_product` as a tuple.