```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and the product of all integers in the list.
    """
    total_sum = sum(numbers)  # Using built-in sum function for calculation
    total_product = 1
    
    # Using a for loop to calculate the total product
    for num in numbers:
        total_product *= num

    return total_sum, total_product


# Testing the function with provided test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and the product of all integers in the list. The sum is calculated using the built-in `sum` function, and the product is calculated using a for loop. The script also includes test cases to verify the correctness of the function.