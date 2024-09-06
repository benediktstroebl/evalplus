```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Parameters:
    strings: list of strings
    Returns:
    string (if there is exactly one string in the list, all the same length, otherwise None)
    """
    if not strings:
        return None

    # we first try to sort the list
    # and return the first string in it
    # if that doesn't work, then we use a custom implementation
    # (because we don't want to depend on a library, and a sorting function)
    try:
        strings.sort()
        # in(('list', 'sort'), 'ord')
        return strings[0]
    except:
        return max(strings, key=len)
```
The code defines a function called `longest` that takes a list of strings as input and returns the longest string present in the list. The function first checks if the strings list is empty, and if it is, it returns None. Otherwise, it sorts the strings list, or uses the `max` function with the `len` key function, as the longest string has the maximum length. The code works by first sorting the strings list and then checks if the `sort` function is available in Python, and if it is, it uses the sorting function to sort the list. If the `sort` function is not available, the code uses the `max` function with the `len` key function, as a fallback option.