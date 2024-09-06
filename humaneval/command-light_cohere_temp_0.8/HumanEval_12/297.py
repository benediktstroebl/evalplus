```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    >>> longest([])
        Trace it raises an error.
    >>> longest(['a'])  
    Traceback (None): File "<ipythonInterpreterHostName>.local>longest: AttributeError: 'list' object does not support item assignment  

    >>> longest(['a', 'b', 'c'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```