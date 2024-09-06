```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the length of the longest string.
    """
    longest = lambda: max(len(string) for string in strings) + 1)
    return longest([])    
```