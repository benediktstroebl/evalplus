```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers representing the sum and product of the input list.
    """
    # Initialize sum and product variables
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current product by the current number
        total_product *= num
    
    # Return a tuple containing the sum and product
    return total_sum, total_product


# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes two variables, `total_sum` and `total_product`, to keep track of these values. Then, it iterates over each number in the list, adding it to `total_sum` and multiplying it with `total_product`. Finally, it returns a tuple containing the calculated sum and product. The script includes example usage at the end to demonstrate its functionality.