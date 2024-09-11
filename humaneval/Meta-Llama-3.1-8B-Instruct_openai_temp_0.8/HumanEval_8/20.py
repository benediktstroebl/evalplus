### Calculating Sum and Product of a List of Integers
#### Problem Statement
Create a Python function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all integers in the list. The sum should be 0 for an empty list and the product should be 1 for an empty list.

#### Solution
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a list.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and product of all integers in the list.
    """
    # Initialize sum and product with neutral elements (0 and 1) respectively
    total_sum = 0
    total_product = 1
    
    # Iterate over the list to calculate sum and product
    for num in numbers:
        total_sum += num
        total_product *= num
    
    # Return the sum and product as a tuple
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
```

This script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of all integers in the list. It uses a for loop to iterate over the list and update the sum and product variables accordingly. The function returns the sum and product as a tuple. The test cases at the end demonstrate the function's behavior for empty lists and non-empty lists.