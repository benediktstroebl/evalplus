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
1. If the input list is empty, it returns the default values of sum and product which are (0, 1).
2. If the list is not empty, it:
    - Calculates the sum of all integers in the list using the `sum` function.
    - Calculates the product of all integers in the list using a list comprehension `sum(n * n for n in numbers)`. 

The code includes type annotations and type hints to improve code readability and provide hints to the Python interpreter about the expected inputs and return values. 

To execute the code simply run the file. The script above is self-contained and does not require any additional dependencies or libraries to run.