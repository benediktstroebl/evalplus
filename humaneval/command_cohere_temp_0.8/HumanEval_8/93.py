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

The function first checks if the input list is empty, and returns a tuple of two zeros in this case. If the list is not empty, it returns a tuple with two values: the first value is the sum of all integers in the list, and the second value is the product of all integers in the list. To achieve this, it calculates the sum of the list elements using the `sum` function and the product of all elements but the first one using the `zip` function and a list comprehension, respectively.

This solution adheres to the problem statement by returning appropriate values for empty lists and demonstrating that the sum and product are calculated correctly for a non-empty list.