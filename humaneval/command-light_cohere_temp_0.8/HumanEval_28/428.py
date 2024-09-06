```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""

    return ''.joinn(strings, sep='')

# Tests
strings = ['a', 'b', 'c']
test_concat = concatenate(strings)
assert test_concat == 'abc', "Function failed test"
```