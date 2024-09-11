```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and the product of all integers in the list.
    """
    # Initialize sum to 0 (empty sum) and product to 1 (empty product)
    sum_result = 0
    product_result = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the sum
        sum_result += number
        # Multiply the current number with the product
        product_result *= number

    # Return the sum and product as a tuple
    return sum_result, product_result


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```