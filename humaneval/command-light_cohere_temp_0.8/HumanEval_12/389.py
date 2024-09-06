```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.

    >>> long['abc']
    return 'abc'
    >>> long(['abc', 'abc'])
    'abc'
    >>> long(['abc', 'abc', 'abc'])
    'abc'
    >>> long(['a', 'bb'])
    Traceback (most recent call last):
      File "<string>", line 9, in longest
    TypeError: cannot convert 'a' to str
    >>> longest(['abc', 'a'])
    Traceback (most recent call last):
      File "<string>", line 9, in longest
    TypeError: cannot convert ['abc'] to str
    """
    return str(max(strings, default=''))
```