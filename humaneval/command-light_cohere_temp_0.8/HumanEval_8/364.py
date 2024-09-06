Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Args:
    numbers (List[int]): A list of integers.
    Returns: A tuple of the sum and product of the list of integers.
    Returns: (0, 1) if the input is empty.
    """
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

tests = [
    """
    Input: [1, 2, 3, 4]
    Output: (6, 24)
    
    Input: []
    Output: (0, 1)
    
    Input: [10]
    Output: (10, 1)
    
    Input: [1, 2, 3, 4, 5]
    Output: (15, 120)
    
    Input: [5]
    Output: (5, 5)
    
    Input: [1, 2, 3]
    Output: (8, 6)
    
    """ + "\n"
    sum_product([]) == (0, 1)
    sum_product([1, 2, 3]) == (8, 6)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function returns a sum and product of the list, or (0, 1) if the list is empty. The test cases demonstrate the example usage of the function.