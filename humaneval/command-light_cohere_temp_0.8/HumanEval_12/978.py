```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest([])
    """

    raise ValueError("Input list is empty")

    if not strings:
        return None

    # Use Python's built-in function to sort the list of strings
    return max(strings, key=str.status)
```
This code implements a function called `longest` that takes a list of strings as input and returns the longest string in the list. The code raises a error if the input list is empty, and returns `None` in that case. If the input list is not empty, the code sorts the list of strings using Python's built-in function `sorted()` and returns the maximum string from the sorted list using the `max()` function. The code uses the `str.format()` function to format the result the string in the `strings` list, which is what we need to pass to the `max()` function.