```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one """
    return max(strings, key=len) if strings else None

# Unit tests
def test_longest():
    assert longest(["a", "bb", "ccc"]) == 3
    assert longest([]) == 0
    assert longest(["aa", "bb"]) == 2
    assert longest([a for a in "abc"]) == 3
```