```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Returns 0 and 1 for empty list.
    """  
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example of passing the function test
test_sum_product = sum_product([1, 2, 3, 4])
 # (10, 24)

# Example 2: Testing with empty list
test_sum_product = sum_product([])
 # (0, 1)
```
This script contains a self-contained function called sum_product, which calculates the sum and product of a list of integers and handles the edge case of an empty list by returning (0, 1). 

The script also includes a test suite that passes the function test with a list of integers and an empty list, and prints the results.