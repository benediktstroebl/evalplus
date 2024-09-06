```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the longest string in a list.

    Args:
        strings (list of strings): The input list of strings.
   
    Returns:
        The longest string in the list, returns it.
    """
    return max(strings, key=len)

# Test cases
strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'

strings = ['xx', 'xx', 'xxx']
assert longest(strings) == 'xx'

strings = []
assert longest(strings) is None
```