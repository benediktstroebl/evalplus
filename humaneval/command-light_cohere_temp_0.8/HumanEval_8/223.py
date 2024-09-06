```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list.
    Numbers should be sorted in ascending order for correct result.
    >>> sum_product([4, 1, 2, 3])
    (6, 12)
    >>> sum_product([5, 10, 50])
    (55, 500)
    >>> sum_product([1, 2, 9])
    (10, 18)
    """
    numbers = sorted(numbers)  # Ensure sorted order
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
```