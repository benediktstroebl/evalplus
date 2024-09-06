```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in the list.
    Input: List[int] containing integers
    Output: Tuple[sum, product]
    Test case:
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    Test case 2:
    >>> sum_product([])
    (0, 1)
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
```