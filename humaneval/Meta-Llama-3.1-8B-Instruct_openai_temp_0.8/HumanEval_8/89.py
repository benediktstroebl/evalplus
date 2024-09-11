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
    sum_of_numbers = 0
    product_of_numbers = 1

    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number

    return sum_of_numbers, product_of_numbers

# Example usage:
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input list. It uses a loop to iterate over the input list, adding each number to the sum and multiplying the product by each number. If the input list is empty, the sum is initialized to 0 and the product is initialized to 1, as required by the problem statement.