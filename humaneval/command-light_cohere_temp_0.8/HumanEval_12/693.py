```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    """
    return max(strings, key=len)
# Test case 1
strings = ['a', 'b', 'c']
assert longest(strings) == 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'

# Test case 3 (empty input list)
strings = []
assert not longest(strings) is None
```