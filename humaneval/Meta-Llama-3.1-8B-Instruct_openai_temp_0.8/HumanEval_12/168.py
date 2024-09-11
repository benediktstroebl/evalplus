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
        return None  # Return None for an empty list

    longest_str = max(strings, key=len)
    return longest_str  # Return the longest string


# Example usage:
if __name__ == "__main__":
    print(longest([]))  # None
    print(longest(['a', 'b', 'c']))  # 'a'
    print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. In case of multiple strings with the same maximum length, it returns the first one encountered. If the input list is empty, it returns `None`. The script also includes example usage at the end.