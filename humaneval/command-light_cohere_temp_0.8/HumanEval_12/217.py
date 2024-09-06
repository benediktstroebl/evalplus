```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    >>> strings = ['a', 'b', 'c']
    return max(strings) if strings else None
    >>> strings = ['a', 'bb', 'ccc']
    return max(strings)
    >>> strings = []
    >>> longest(strings)
    None
    >>> strings = ['aa', 'a', 'bb', 'ccc']
    >>> longest(strings)
    'aa'
    """

    # Ensure even length
    if len(strings) == 0:
        return None

    return max(strings, key=len)
```  The function checks if the input list is empty, returns None. If not empty, it uses the `max` function with a custom key function `len` to find the maximum length of characters.