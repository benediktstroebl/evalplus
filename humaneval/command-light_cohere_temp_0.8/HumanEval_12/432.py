```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string from a list of strings.
    Parameters:
    strings: List[str] -> List[str]
        List of strings to compare their lengths.
    Returns: the longest string found in the list.
    Returns: None if the input list is empty.
    """
    test cases
   
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    >>> longest([''])
    """
    if not strings:
        return None
    return max(strings, key=len)
```