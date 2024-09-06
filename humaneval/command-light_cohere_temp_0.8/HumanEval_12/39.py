```python
from typing import List
def longest(strings: List[str]): 
    """ Returns the longest string in the list """
    if not strings:
        return None
    return max(strings, key=len)

# Unit tests
def test_longest():
    """ Unit tests for the longest function """
    strings = ['a', 'b', 'c']
    assert longest(strings) == 'c'
    strings = ['a', 'bb', 'ccc']
    assert longest(strings) == 'ccc'
    strings = []
    assert longest(strings) is None
    strings = ['a', 'bb', 'ccc']
    assert len(strings) == 3
    strings = ['abc', '123', 'abc']
    assert longest(strings) == 'abc'

if __name__ == "__main__":
    test_longest()
```
The code defines a function `longest` that calculates and returns the longest string from a list of strings. It also includes a test suite with a series of tests to validate the correctness of the `longest` function.