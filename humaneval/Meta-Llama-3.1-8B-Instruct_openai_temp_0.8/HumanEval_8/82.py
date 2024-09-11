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
    # Initialize sum and product to 0 and 1 respectively, as per the problem statement
    total_sum = 0
    product = 1

    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current product by the current number
        product *= num

    # Return the total sum and product as a tuple
    return total_sum, product

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes the sum and product to 0 and 1, respectively, and then iterates over each number in the list, adding it to the sum and multiplying it with the product. Finally, it returns the sum and product as a tuple. The script also includes example use cases to demonstrate the function's behavior.