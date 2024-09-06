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
    return (sum(numbers), sum(numeras[0:1] for numeras in numbers))
```

The function works as follows:
- It utilizes the `typing` module to define the input as a list of integers and the output as a tuple containing an integer sum and integer product.
- If the input list is empty, it returns `(0, 1)` according to the problem statement.
- Iterates through the list and uses the `sum` function to calculate the sum of the integers, and the `sum` function with a generator expression to calculate the product of the integers. 

You can demonstrate this using the `>>>` symbol to assert the examples provided in the problem statement.