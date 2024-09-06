Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Args: strings (List[str]): List of strings.
    Returns: first string with the same length or None if empty list.
    Returns: first matching string, or None if no match.
    """
    string: str
      if not strings:
        return None
    i = 0
    max_len = 0
    for string in strings:
        if i >= len(string):
            break
        if len(string) == max_len:
            max_len = string
        i += 1
    return max_len
```

This code is a Python program that aims to find the longest string in a given list. It uses a `typing` to provide type hints for the function signature and provides information about the return values of the function.