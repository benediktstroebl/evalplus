```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)  # Calculate the sum of the numbers in the list
    product = 1  # Initialize the product to 1 (neutral element for multiplication)
    for number in numbers:  # Iterate over the numbers in the list
        product *= number  # Multiply the current product by the current number
    return total_sum, product  # Return the sum and product as a tuple

# Example use cases:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
```