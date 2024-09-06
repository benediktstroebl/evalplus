```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list
    
    >>> sum_product([]) (0, 1)
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    if not numbers:  # handle empty list
        return (0, 1)
    return (sum(numbers), sum(numbers * x for x in numbers))
```