```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list.
    """
    strings = [ 'ab', 'bc', 'abc', 'abc' ]
    return max(strings, default=None)

# Test the function
for _ in range(10):
    actual = longest(['a', 'bb', 'ccc'])
    if actual != 'ccc':
        print(f"Expected {'ccc'}, but was {actual}.")
```