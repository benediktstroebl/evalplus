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
    # Initialize sum and product with identity values for sum (0) and product (1)
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```
This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the input list. It initializes the sum and product with identity values (0 for sum and 1 for product) and then iterates over the input list, updating the sum and product accordingly. The function returns the total sum and product as a tuple. The script also includes test cases to verify the correctness of the function.