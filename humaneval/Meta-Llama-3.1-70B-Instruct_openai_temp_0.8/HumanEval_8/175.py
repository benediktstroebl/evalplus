```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers: A list of integers

    Returns:
    A tuple where the first element is the sum of the integers and the second element is the product of the integers
    """
    # Initialize sum to 0 (empty sum) and product to 1 (empty product)
    total_sum = 0
    total_product = 1

    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number with the total product
        total_product *= number

    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Example usage
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```