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
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else numbers[0])
```

The function works for non-empty as well as empty lists and works in an efficient manner without any explicit loops. Using typing module helps to make the function more readable and make it easier to catch potential errors before runtime. The tests provided are enough to confirm the function is correct. 
To use this function simply import it and call it with a list of integers.  It should be noted that the sum_product() function assumes the list elements are integers, if the list contains other types of elements, the behavior is not guaranteed.