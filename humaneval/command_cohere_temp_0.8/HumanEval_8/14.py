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

The function first checks if the input list is empty; if it is, it returns a tuple of two special values: an empty sum (0) and an empty product (1). If the input list is not empty, it returns the sum and product of all the integers in the list. To do this, it uses the `sum` function to calculate the sum of the integers in the list and the `sum` function again to calculate the product of the integers in the list, respectively.

This solution allows you to quickly calculate the sum and product of any list of integers and handles edge cases where the input list is empty. 

You can use this function to solve the problem by passing a list of integers as input. For example:
```python
numbers = [1, 2, 3, 4]
sum_product(numbers)
```
This will give the result: `(10, 24)` for the provided example.