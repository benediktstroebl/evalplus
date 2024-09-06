```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculates the sum and product of a list of integers.
   
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5, 10, 20, 30])
    (45, 900)
    """
    if not numbers:
        return (0, 1)
    sum_ = 0
    product = 1
    for num in numbers:
        sum_ += num
        product *= num
    return (sum_, product)
```