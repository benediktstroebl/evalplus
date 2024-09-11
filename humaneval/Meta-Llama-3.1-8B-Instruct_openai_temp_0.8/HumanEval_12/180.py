```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings
    
    Returns:
    Optional[str]: The longest string in the list or None if the list is empty
    
    Examples:
    >>> longest([])
    >>> 
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # check if the list is empty
        return None
    
    max_length = 0
    longest_str = strings[0]
    
    for string in strings:
        if len(string) > max_length:  # if a string is longer than the current max
            max_length = len(string)  # update max_length
            longest_str = string  # update longest_str
    
    return longest_str
```

This script first checks if the input list is empty. If it is, it returns `None`. If not, it iterates over the list, keeping track of the longest string it has seen so far. If it finds a string that is longer than the current longest string, it updates the longest string. Finally, it returns the longest string it has found.