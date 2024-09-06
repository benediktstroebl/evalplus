```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    >>> print(sum_product([5, 15, 7, 6]))
    (22, 56)
    """
    if not numbers:
        return (0, 1)
    
    return (sum(numbers), product(numbers))

```

This script defines a function 'sum_product' which takes a list of integers as input and returns a tuple with the sum and product of the list. The function first checks if the empty list is passed and returns 0 and 1. The product is calculated using the built-in function product. The sum is calculated using the built-in function sum.