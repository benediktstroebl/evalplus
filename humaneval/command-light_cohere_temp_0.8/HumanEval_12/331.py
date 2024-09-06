```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    strings = [
        'hello', 
    "world", 
    "is", 
    "out", 
    "long", 
    "text"
    ]
    return max(len(x) for x in strings)
```