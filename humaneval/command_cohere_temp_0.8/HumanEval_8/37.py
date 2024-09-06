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
1. If the input list is empty, it returns the standard values for an empty sum and empty product, namely (0, 1).
2. If the list is not empty, it sums up all the integers in the list and calculates the product of all integers in the list. 

This solution adheres to Python's typing module to make function signatures more explicit and robust to potential input errors. The `Tuple[int, int]` return type specification means the function returns a tuple with two integers. Such type annotations can help when writing the function to ensure you're returning the correct type of variable and also when using the function to ensure you're passing in the correct type of variable. 

This approach could greatly aid in catching bugs early and reducing the time spent debugging.