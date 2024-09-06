```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    """
    First, check if the list is empty, and return None
    """
    if not strings:
        return None

    # Sort the strings in alphabetical order
    strings.sort()
    longest_string = max(strings, key=len)
    return longest_string

# Unit tests
def test_longest():
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['aa', 'bb', 'ccc']) == 'ccc'
    assert longest([]) == None
    assert longest(['abcd']) == 'abcd'
```
This code implements a function named `longest` that takes a list of strings as input and returns the longest string from the list. The `test_longest` function verifies the functionality of the `longest` function with a set of test cases.