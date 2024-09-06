```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string.
    >>> return longest(['a', 'b', 'c'])
    'a'
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> return longest([])
    None
    """
    # Use string comparison to find the longest string
    max_length = max([len(string) for string in strings])
    longest_string = strings[0]
    for string in strings:
        if len(string) == max_length:
            longest_string = string
    return longest_string
```