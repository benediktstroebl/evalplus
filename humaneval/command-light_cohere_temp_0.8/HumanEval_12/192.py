```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Return the longest string from a list of strings.
    """
    strings = [
        "Hello"
        , "World"
        , "Python"
        ,"Python3"
    ]
    return max(strings, key=len)
```