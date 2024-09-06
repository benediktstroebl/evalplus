```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    Args: strings (list of strings)
    
    Returns:
        The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Unit tests
def test_longest():
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest([]) == None
```
The provided solution passes all tests. It uses the standard Python functionality with typing and basic functional programming to solve the problem of finding the longest string in a list. It also has comprehensive unit tests to ensure the functionality of the `longest` function.