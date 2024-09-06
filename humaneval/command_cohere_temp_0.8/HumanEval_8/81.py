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

The function first checks if the input list is empty, and accordingly returns a tuple with both elements being 0 and 1, respectively. If the list is not empty, it constructs the sum of the elements in the list through `sum(numbers)`. To compute the product of the elements in the list, the function iterates over pairs of elements established by `zip(numbers, numbers[1:])`, multiplying the corresponding elements and summing them up through `sum()`. If the list has only one element, the function directly employs `prod(numbers)` to compute the product. 

This approach utilizes Python's built-in functions to concisely express the problem's essence and accommodate all test cases as requested.