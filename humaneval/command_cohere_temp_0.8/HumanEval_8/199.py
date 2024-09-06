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
    return (sum(numbers), sum(n * n for n in numbers))
```

The function checks if the input list is empty, and accordingly returns a tuple with 0 and 1 for sum and product, respectively. Meanwhile, if the input list is not empty, the function proceeds to calculate the sum and product of the integers and returns the result as a tuple. The desired behavior is encapsulated in the `sum_product()` function, ready to be used.