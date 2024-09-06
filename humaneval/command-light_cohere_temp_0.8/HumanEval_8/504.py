```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of all the integers in a list
    >>> sum_product([])
    Traceback (most recent call last):
    File "your_script.py", line: 7
    File "your_script.py", line: 6
    Definition 'numbers' is undefined
    File "your_script.py", line: 10
    File "your_script.py", line: 5
    [int]
    File "your_script.py", line: 13
    File "your_script.py", line: 4
    NameError: name 'numbers' was not defined
    """
    if not numbers:
        return 0, 1
    return sum(numbers), product(numbers)

def product(numbers: List[int]) -> Tuple[int]:
    """
    >>> product([])
    (1,0)
    >>> product([1, 2, 3])
    (3, 6)
    """
    if not numbers:
        return (0, 1)
    return sum(numbers) * sum(numbers)
```