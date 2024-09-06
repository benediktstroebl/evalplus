```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates sum and product of integers in a list.
    If the list is empty, return (0, 1) 
    Otherwise, iterate through list, accumulate sum and product, and return it.
    """
return sum(numbers[:-1]), product(numbers[:-1])

#Test cases
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)
```