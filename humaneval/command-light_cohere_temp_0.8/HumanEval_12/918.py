```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string.
    >>> return None if the only empty list
    >>> longest([])
    """
    return max(strings, key=len) if strings else None

# Test the function
def test():
    strings = ['a', 'bb', 'ccc']
    assert longest(strings) == 'ccc'
test()
```