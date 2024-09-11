```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([]) is None
    True
    >>> longest(['a', 'b', 'c']) == 'a'
    True
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    True
    """
    if not strings:
        return None
    return max(strings, key=len)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `longest` which takes a list of strings and returns the longest one. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. 

The `max` function with the `key` argument is used to find the longest string. The `key` argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, the `len` function is used to extract the length of each string. 

The `if __name__ == "__main__":` block is used to run the doctests when the script is run directly. The doctests are used to test the function and ensure it behaves as expected.