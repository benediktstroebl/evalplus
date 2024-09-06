```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    list must be passed as a parameter, as well as all strings in the list must be equal to str.
    if not strings:
        return None
    # sort the strings
    return max(strings, key=len)
def test_longest() -> None:
    """ Test case function that checks the correctness of the longest function"""
    strings = ['a', 'bb', 'ccc']
    result = longest(strings)
    assert result == 'ccc'
```