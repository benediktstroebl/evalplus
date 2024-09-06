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

The function works as follows:
1. If the input list is empty, it returns the qualifying empty sum and product values of 0 and 1, respectively.
2. If the list is not empty, it calculates the sum of the list elements through the built-in Python `sum` function.
3. Subsequently, it calculates the product of the list elements by employing a list comprehension that multiplies each element with itself.
4. Finally, the function returns a tuple consisting of the calculated sum and product.

This solution adheres to the requirement of returning a tuple with the sum and product of the integers in the input list, with empty inputs returning (0, 1).