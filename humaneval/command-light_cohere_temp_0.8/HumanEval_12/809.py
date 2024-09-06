```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list.
    """
    # Return a first string in the list that is longer than any other string in the list
    return strings[0] if max(map(len, strings)) == len(strings[0]) else None
    """

def test_longest():
    """
    Test case: return the longest string from ['a', 'bb', 'ccc']
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```