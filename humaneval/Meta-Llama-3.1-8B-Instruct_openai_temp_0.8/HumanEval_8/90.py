```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and the product of the given integers.
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num

    # Return the total sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function iterates over each number in the list, adding it to the sum and multiplying it with the product. If the list is empty, it returns 0 and 1 as the sum and product respectively. The function is then tested with an empty list and a list with some numbers.