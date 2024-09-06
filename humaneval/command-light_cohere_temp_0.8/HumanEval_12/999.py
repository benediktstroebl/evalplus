```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.

    Args:
    strings (list[str]): list of strings

    Returns:
    str, the longest string
    """
    return max(strings) if strings else None
```
This code provides a solution to the problem, the longest function takes a list of strings as input and returns the longest string in the list. It uses the maximum function to get the maximum value of all strings and returns the longest one.