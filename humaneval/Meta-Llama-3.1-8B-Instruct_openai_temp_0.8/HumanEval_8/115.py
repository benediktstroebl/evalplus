```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product variables with default values for empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over the input list to calculate sum and product
    for num in numbers:
        total_sum += num
        total_product *= num
    
    # Return the calculated sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. The function uses a simple iterative approach to calculate the sum and product. If the input list is empty, it returns the default values of 0 for the sum and 1 for the product. The script also includes test cases to verify the correctness of the function.