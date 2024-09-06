```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute sum and product for a given list of integers.
    >>> # Test case: empty list
    assert sum_product([]) == (0, 1)
    >>> # Test case: list with single element
    assert sum_product([1]) == (1, 1)
    >>> # Test case: list with 2 elements
    assert sum_product([1, 2]) == (2, 2)
    >>> # Test case: list with more than 2 elements
    assert sum_product([1, 2, 3, 4]) == (6, 12)
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```