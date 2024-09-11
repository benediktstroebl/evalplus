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
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the input list
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        # Multiply the total product by the current number
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

This script defines the `sum_product` function, which calculates the sum and product of a given list of integers. The function initializes the sum and product with default values (0 and 1, respectively) to handle the case where the input list is empty. It then iterates over each number in the list, adding it to the total sum and multiplying it with the total product. Finally, the function returns the total sum and total product as a tuple.

The script also includes test cases to demonstrate the function's behavior with an empty list and a non-empty list.