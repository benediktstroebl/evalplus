```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list of strings.
    Args: strings (list of strings)
    Returns:
        The longest string in the list of strings.
    """
    list contains at least string
    if not strings:
        return None
    # sort the strings in alphabetical order
    strings.sort_str = ''.join(strings)
    longest_str = strings[0]
    for i in range(1, len(strings)):
        if strings[i] > longest_str:
            longest_str = strings[i]
    return longest_str
```