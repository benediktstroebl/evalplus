```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = 0
    total_product = 1

    for num in numbers:
        total_sum += num
        total_product *= num

    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function initializes the sum to 0 and the product to 1, then iterates over the list, adding each number to the sum and multiplying each number with the product. Finally, it returns the sum and product as a tuple.

The script also includes two test cases to verify the correctness of the function. The first test case checks the function with an empty list, and the second test case checks the function with a list of integers.