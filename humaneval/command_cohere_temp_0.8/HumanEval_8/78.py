```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else prod(numbers))
```

The function prod() is used to calculate the empty product whereas the sum() along with a zip() is used to calculate the sum and product of non-empty lists. This solution is efficient and easy to understand.

Here is an example of how to test this function:
```python
def test_sum_product():
    """ Test the correctness of the sum_product function"""
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([-2, -1, -4, -3]) == (-13, -60)
    assert sum_product([0, 0, 0]) == (0, 1)
``` 

This function will output a test report.