```markdown
### Solution to the Problem

Here's a Python script that solves the problem using Python's built-in `math.prod` function to handle the edge case where the product of an empty list is 1:
```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the input list.
    """
    # Calculate the sum of the list using the built-in sum function
    total_sum = sum(numbers)
    
    # Use math.prod to calculate the product of the list
    # If the list is empty, math.prod will return 1
    total_product = math.prod(numbers)
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```
This script uses Python's built-in `sum` function to calculate the sum of the list and the `math.prod` function to calculate the product of the list. The `math.prod` function handles the edge case where the list is empty by returning 1. The script also includes test cases to verify its correctness.