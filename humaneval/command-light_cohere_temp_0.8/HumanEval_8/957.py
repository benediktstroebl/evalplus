```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    If the function returns a tuple with a sum and product of the numbers passed.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return (0, 1) if not numbers else (sum(numbers), product(numbers))

# Test cases with comments
>>> test_sum_product([])
Exception (TypeError): 'argument 'numbers' has unexpected subscript 1'
>>> test_sum_product([1, 2, 3])
(3, 6)
>>> test_sum_product([10, 20, 30])
(60, 900)
``` 
This Python code defines a function called `sum_product` that calculates the sum and product of a list of integers. The function utilizes the simple logic to return `None` if the input list is empty, and otherwise returns the sum and product of the list's elements using the built-in `sum` and `product` functions. 
The function includes a type hint using `typing. `List function for better code that it allows the function to be used with the `List` and `Tuple` classes.