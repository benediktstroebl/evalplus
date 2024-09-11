```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Example usage:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This Python script defines a function `longest` that takes a list of strings and returns the longest one. If there are multiple strings of the same length, it returns the first one encountered. If the input list is empty, it returns `None`. The function uses the built-in `max` function with the `key` parameter set to `len`, which allows it to find the longest string based on its length. The example usage at the end demonstrates how to use the function with different inputs.