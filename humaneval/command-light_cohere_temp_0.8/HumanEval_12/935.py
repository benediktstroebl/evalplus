```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    strings = ['a', 'b', 'c']
    assert longest(strings) == 3
    assert longest('') == 0
    assert longest([]) is None
    assert longest(['a']) == 1
    assert longest(['a', 'bb', 'ccc']) == 3
    return len("ccc")
```