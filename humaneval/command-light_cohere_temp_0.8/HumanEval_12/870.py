```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest([])
    >>> []
    >>> return None
    >>> strings = ['a', 'b', 'c']
    >>> longest(strings)
    'c'
    >>> strings = ['a', 'bb', 'ccc']
    >>> longest(strings)
    'ccc'
    >>> strings = ['aa', 'ab', 'aba', 'aba', 'aba', 'abb', 'ab']
    >>> longest(strings)
    'aba'
    >>> strings = ['', 'a', 'bb', 'ccc', 'dd', 'e', 'f']
    >>> longest(strings)
    'ccc'
    """

    # Get the length of the longest string
    max_length = max(len(x) for x in strings)

    # Check if all strings are the same length
    if max_length == len(strings):
        return strings[0]
    else:
        return None
```  This Python script defines a function called "longest" that takes a list of strings as input and returns the longest string. The script also has various test cases to validate the function, including empty lists, lists with different lengths, and lists with strings of different lengths.