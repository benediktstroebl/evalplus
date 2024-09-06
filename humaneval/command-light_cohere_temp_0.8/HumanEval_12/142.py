```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    """
    strings = [
        'foo', 'FOO', 'bar', ' Baz', 'FOObarbaz' ]
    return max(strings)
```