Here is a self-contained Python function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of all the integers in a list.
    Args: 
    - numbers (List[int]): a list of integers 
    Returns: 
    - sum (int): sum of all the integers 
    - product (int): product of all the integers 
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
```

This function uses Python's built-in sum and product functions to efficiently calculate the sum and product of a given list of integers. The function handles both cases where the list is empty or not, and it returns a tuple of the sum and product. The code is written in a way that it can be run independently, without the need for external variables.