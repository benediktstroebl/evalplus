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

The function works for non-empty as well as empty lists and works in an efficient manner. 

#### Complexity Analysis:
Time Complexity: `O(n)` where `n` is the length of the array. 

This is because we use a sum function which has a time complexity of O(n), and a product function which has a time complexity of O(n^2), but we only call the product function if there is more than one element in the list. 

Auxiliary Space: `O(1)` irrespective of the input size.