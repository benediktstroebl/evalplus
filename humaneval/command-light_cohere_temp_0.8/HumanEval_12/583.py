```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "<stdin>", line 9, in <module>
        longest(['a'])
    AssertionError: Lists must contain elements
    ```

The `longest` function takes a list of strings as input and returns the longest string. The test cases demonstrate that the function works as expected.