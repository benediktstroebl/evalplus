```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, returns the longest one. """

    return max(strings, key=len)
strings = ['a', 'bb', 'ccc']
print( longest(strings) )
```