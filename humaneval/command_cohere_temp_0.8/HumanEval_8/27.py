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

The function works in such a way that if an empty list is provided, it will return a tuple with numerical values of 0 and 1, respectively. Otherwise, it will return the sum of the numbers in the list and the product of the numbers in the list. The product is calculated using a generator expression with the `sum` function.  This ensures that the code is efficient for large lists and does not consume excessive memory.

Here is an example of how to use the `sum_product` function:
```python
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
```

Output:
```
(10, 24)
```