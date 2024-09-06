```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    Args:
        strings (list of strings) -> List[str]
    Returns:
        str: longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)
# Unit tests
def test_longest():
    longest(['a', 'b', 'c']) == 'a'
# Run the tests
test_longest()
```