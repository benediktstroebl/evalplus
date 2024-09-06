```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string in the list.
    >>> longest(['a'])
    # return 1
    >>> longest(['a', 'bb', 'ccc'])
    # return 3
    >>> longest(['a'])
    # return 1
    >>> longest(['a', 'aa'])
    # return 2
    >>> longest(['aa', 'a'])
    # return 2
    >>> longest(['a', 'bb', 'ccc'])
    # return 3
    >>> longest([])
    # return 0
    >>> longest(['aa', 'a', 'bb', 'ccc'])
    # return 3

    return max([len(x) for x in strings])
```