```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates sum and product of a list of integers.
    return: (sum, product)
    >>> sum_product([]) 
    ()
    >>> sum_product([1, 2, 3, 4]) 
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```