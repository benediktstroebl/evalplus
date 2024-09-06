```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    
    # Using str.maketransformer
    implemented on Python 3, we can do it in one pass without the need to convert all strings to lowercase.
    return max(strings, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc'])))
print(longest([''))))
print(longest([])))
``` 
This script provides a self-contained solution and test cases for finding the longest string in a list of strings, using the `longest()` function. The function also checks for an empty list and returns `None` in that case.