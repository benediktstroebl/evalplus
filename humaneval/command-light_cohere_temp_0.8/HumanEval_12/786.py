```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    :return max(strings, default='')
    """
    return max(strings, default='')

# Test case 1
strings = ['a', 'b', 'c']
result = longest(strings)
assert result == 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
result = longest(strings)
assert result == 'ccc'

# Test case 3
empty_strings = []
result = longest(empty_strings)
assert result is None
```