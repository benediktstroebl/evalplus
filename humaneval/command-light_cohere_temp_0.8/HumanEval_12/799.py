Here is a Python script with a self-contained function that solves the problem of returning the longest string from a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    """
    list of strings and return the first one that is not None
    """
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in that list, using the `max` function with the `key` argument set to the length of strings.

It uses the `typing` module to provide type hints for the input parameter and the return value. This helps to improve code readability and maintainability of code.