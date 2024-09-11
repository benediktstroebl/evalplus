```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple where the first element is the sum of the list and the second element is the product of the list.
    """
    # Initialize sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number with the total product
        total_product *= number
    
    # Return a tuple of the total sum and the total product
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Should print (0, 1)
print(sum_product([1, 2, 3, 4]))  # Should print (10, 24)
```

This script meets the requirements by implementing the `sum_product` function which calculates the sum and product of a list of integers and returns them as a tuple. It also includes test cases to verify its correctness. The function initializes the sum and product to 0 and 1 respectively, then iterates over each number in the list, updating the sum and product accordingly. Finally, it returns the sum and product as a tuple.