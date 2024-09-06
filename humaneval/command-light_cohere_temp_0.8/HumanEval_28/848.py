```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
# Unit tests
strings = ['a', 'b', 'c']
expected = 'abc'
assert concatenate(strings) == expected
strings = []
strings = ['a', 'aa', '∗∗∗']
expected = 'aa∗∗∗'
assert concatenate(strings) == expected
```