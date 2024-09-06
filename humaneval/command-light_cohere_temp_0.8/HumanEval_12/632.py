```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

# Test the function
strings = ['a', 'b', 'c']
assert longest(strings) == 'c'
strings = ['aa', 'bb', 'ccc']
assert longest(strings) == 'ccc'
strings = []
assert not extends longest(strings)
strings = ['a', 'bb', 'ccc']
assert longest(strings) is None
```