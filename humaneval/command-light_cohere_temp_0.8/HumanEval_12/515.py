```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.

    >>> print(longest(["a", "bb", "ccc"]))
    'ccc'

    >>> print(longest(["aa", "ccc", "ab"]))
    'ccc'

    >>> print(longest(["abc", "ab", "ac"]))
    'abc'

    >>> print(longest(["ab", "aac", "abc"]))
    'abc'

    >>> print(longest(["a", "aa", "bb"]))
    'aa'

    >>> print(longest(["abc", "abcd", "acbc"]))
    'abc'

    >>> print(longest(["a"]))
    Traceback (most recent call last):
      File "<string>", line 20, in <module>
    File "<string>", line 6, in longest
    ValueError: input must contain at least one element

False
    """
```