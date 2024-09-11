### Python Script to Calculate Sum and Product of a List of Numbers

```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    
    # Initialize sum and product variables to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and product as a tuple
    return total_sum, total_product


# Test the function with some examples
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, -2, -3, -4]))  # Expected output: (-10, -24)
print(sum_product([5, 0, 5]))  # Expected output: (10, 0)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It then tests this function with some example inputs to demonstrate its correctness.