```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string from the list.
    If a strings is empty, returns None.
    Otherwise, iterates through the strings from longest to shortest and returns the final one.
    """
    test_longest()
    longest(['a', 'bb', 'ccc'])
    """
    if not strings:
        return None
    return max(strings, key=len)

def test_longest():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```