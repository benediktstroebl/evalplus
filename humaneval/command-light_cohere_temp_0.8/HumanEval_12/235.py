```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c'])
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'b'])
    'a'
    >>> longest([''])
    >>> longest(['a', 'b', 'ccc'])(['ccc'])
    'ccc'
    >>> longest([None])
    >>> longest([None, 'a'])
    'None'
    """

def test_longest():
    return [
        ("Passing empty list test", [])
    , ("Passing list with one-item test", ['a'])
    , ("Longest string in list test", ['a', 'bb', 'ccc'])
    , ("Returning None for none input", [None])
    , ("Returning None for list with None only", [None, 'a'])
    ]

# run the function test_longest to print the test results
for test in test_longest():
    print(test)
```