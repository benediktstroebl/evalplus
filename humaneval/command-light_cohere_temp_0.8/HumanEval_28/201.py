Here's the improved Python script:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Join list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)
```  This script defines a `concatenate` function that takes in a list of strings and returns a single string by joining them.  It accepts both empty lists and lists of single string, and joins them into a single string with a space character (' ') as a separator.