Here's the solution:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a', ' ', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    """
    return ''.join(s for s in strings)
```
The code defines a function called `concat` that takes a list of strings as an argument and returns a concatenated string by joining the strings together. The code then demonstrates the result by passing various test cases and prints the expected output for each case.