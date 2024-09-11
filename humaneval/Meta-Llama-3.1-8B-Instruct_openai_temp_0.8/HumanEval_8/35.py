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
    # Initialize sum and product with default values for empty lists
    sum_result = 0
    product_result = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the number to the sum
        sum_result += num
        # Multiply the number with the product
        product_result *= num
    
    # Return the sum and product as a tuple
    return sum_result, product_result


# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a list of integers, and then tests the function with some examples. The function uses a basic loop to iterate over each number in the input list and accumulates the sum and product accordingly. If the input list is empty, the function returns a sum of 0 and a product of 1, as specified in the problem.