```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers.
    """
    total_sum = 0
    total_product = 1
    
    for number in numbers:
        total_sum += number
        total_product *= number
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. The function uses a for loop to iterate over the list, adding each number to the sum and multiplying the product by each number. The function then returns the sum and product as a tuple.

The script also includes test cases to verify that the function is working correctly. The test cases check that the function returns the expected output for an empty list and a list containing the numbers 1, 2, 3, and 4.