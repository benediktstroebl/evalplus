```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of a list of integers.
    return a sum and product of all the numbers in the list, and return a tuple with the sum and product values.
    >>> sum_product([])
    0
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:  # Empty list, return 0 and 1
        return (0, 1)
    
    sum_ = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum_, product)
```