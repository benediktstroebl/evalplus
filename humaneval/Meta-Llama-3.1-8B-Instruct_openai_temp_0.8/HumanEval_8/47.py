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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over the input list and update sum and product
    for number in numbers:
        total_sum += number
        total_product *= number

    # Return the calculated sum and product
    return total_sum, total_product

# Example usage
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This Python script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the input list. The function initializes the sum and product to 0 and 1 respectively, then iterates over the input list to update the sum and product. Finally, it returns the calculated sum and product. The script includes example usage at the end to demonstrate the function's behavior.