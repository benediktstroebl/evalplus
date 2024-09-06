```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.

    If list is empty, return None.
    """

    Check:
    assert not strings
    assert isinstance(strings, List), "Input must be a list"
    return None

strings = ['a', 'b', 'c', 'a']
print(longest(strings))  # Output: c
```