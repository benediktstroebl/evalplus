Here's the Python script with the self-contained function `intersperse()`:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    >>>intersperse([1, 2, 3], 2)
    [1, 2, 2, 3]
    >>> intersperse([1, 2, 3, 4, 5], 3)
    [1, 3, 4, 5, 6]
    """
    return [x + y for x, y in zip(numbers, numbers[1:])]
```
This script defines a function `intersperse` that takes a list of integers `numbers` and a delimiter `delimiter` as input, and returns a new list with the elements of `numbers` interspaced by the given `delimiter`.