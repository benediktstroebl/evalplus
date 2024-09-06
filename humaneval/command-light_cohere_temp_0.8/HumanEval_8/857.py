```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of all the integers in the list.
    Args: 
    - numbers (List[int]) : a list of integers 
    Returns: 
    - tuple (sum, product) consisting of sum and product of integers in numbers list
    """
    if not numbers: # Handle empty list
        return (0, 1)

    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```

This script provides a `sum_product` function that takes a list of integers as input and returns a tuple of the sum and product of all the integers in the list. It handles the essential edge cases for an empty list and returns `(0,1)`, and uses a loop to iterate over the list and calculate the sum and product correctly.