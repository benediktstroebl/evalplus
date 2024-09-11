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
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the sum
        total_sum += num
        # Multiply the current number with the product
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # Should print (0, 1)
print(sum_product([1, 2, 3, 4]))  # Should print (10, 24)
print(sum_product([-1, 0, 1]))  # Should print (0, 0)
print(sum_product([5, 5, 5]))  # Should print (15, 125)
print(sum_product([]))  # Should print (0, 1)
```

This script defines a function `sum_product` that calculates the sum and product of a list of integers. It initializes the sum and product to 0 and 1 respectively, then iterates over the list of numbers, updating the sum and product accordingly. The function returns the sum and product as a tuple. The script includes test cases to demonstrate the function's behavior.