### Sum and Product of a List of Integers

The following Python script solves the problem of calculating the sum and product of a list of integers.

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum is equal to 0 and empty product is equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1

    # Iterate over the input list
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num

    # Return the sum and product as a tuple
    return total_sum, total_product

# Test the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script uses a simple iterative approach to calculate the sum and product of the input list. It initializes the sum to 0 and the product to 1, then iterates over the list, updating the sum and product at each step. Finally, it returns the calculated sum and product as a tuple.