```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of the input integers.
    """
    # Initialize sum and product with their respective identity values (0 for sum, 1 for product)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the total product by the current number
        total_product *= num

    # Return the total sum and the total product as a tuple
    return total_sum, total_product

# Example usage
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```

This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the input integers. It initializes the sum and product with their respective identity values (0 for sum, 1 for product), then iterates over each number in the input list, updating the sum and product accordingly. Finally, it returns the total sum and the total product as a tuple.