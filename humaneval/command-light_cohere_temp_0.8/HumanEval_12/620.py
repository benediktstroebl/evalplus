```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string from a list of strings.
    >>> longest([])
    ^ ??
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'b'])
    Traceback (most recent call last):
      File "<string>", line 6, in longest
    File "<stdin>", line 2, in <module>
    AssertionError: list() evaluates to False
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['aa', 'b']))  # Output: 'aa'
print(longest(['abc', 'a', 'bc']))  # Output: 'abc'
```
This script defines a function `longest` that takes a list of strings and returns the longest string. The test cases ensure that the function works correctly with different scenarios. 

Please note that this code is self-contained and does not require any additional imports or external functions.