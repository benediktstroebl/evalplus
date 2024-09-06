```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of the integers in the list
    >>> sum_product([]) (0, 1) 
    (0, 1)
    >>> sum_product([1, 2, 3, 4])  (10, 24)
    >>> sum_product([5, 6, 7]) (15, 28)
    """
    if not numbers:
        return (0, 1)
    
    sum_ = sum(numbers)
    prod_ = 1
    for num in numbers:
        prod_ *= num
    return (sum_, prod_)
```