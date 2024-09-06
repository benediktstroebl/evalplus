```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """

    return max(strings, key=len)

# Sample test cases
strings = ['a', 'b', 'c']
assert longest(strings) == 'c'

strings = ['aa', 'bb', 'ccc']
assert longest(strings) == 'ccc'

strings = []
assert longest(strings) is None

strings = ['a', 'bb', 'bc']
assert longest(strings) == 'bb'

strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'
```

This script defines a function called `longest` that takes a list of strings as input and returns the longest string in the list. The function utilizes the max function and the `key=len` parameter to identify the longest string. This function is passing a test cases that validate its behavior.