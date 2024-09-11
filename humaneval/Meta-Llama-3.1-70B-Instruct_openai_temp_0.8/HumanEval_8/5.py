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

    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the total product by the current number
        total_product *= num

    # Return the total sum and the total product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and the product of all integers in the list. It initializes the sum and product with default values (0 and 1, respectively) to handle the case where the input list is empty. The function then iterates over the list, adding each number to the sum and multiplying the product by each number. Finally, it returns the total sum and the total product as a tuple.

The script also includes test cases to verify the correctness of the function. The test cases cover the cases where the input list is empty and where the input list contains multiple integers.