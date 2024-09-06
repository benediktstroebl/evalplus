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
    return (sum(numbers), sum(numeries[0:1] for numeries in numbers))
```

The function works as follows:
- It checks if the input list is empty;
- If the list is empty it returns the standard "empty product" and "empty sum" values of (0, 1);
- Otherwise, it builds the sum of the list as the sum of all elements in the list;
- It builds the product of the list as the product of all elements in the list, ensuring that the empty product is interpreted as 1. 

The tests will look as follows:
```python
def test_sum_product():
    """Test the sum_product function."""
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([]) == (0, 1)
    assert sum_product([0, 0, 0]) == (0, 0)
    assert sum_product([2, 4, 6, 8]) == (20, 240)
    assert sum_product([-1, -2, -3, -4]) == (-10, -24)
```