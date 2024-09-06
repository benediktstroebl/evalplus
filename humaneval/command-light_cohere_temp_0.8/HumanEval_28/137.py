```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of string
    Returns:
        string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The provided code includes a function **concatenate** that takes a list of strings as an argument and returns the concatenated string. It also has a test function with various test cases and ensures that the result is correct.

The time complexity of this solution is O(n), where n is the length of the input list. The space complexity is O(1), as it does not require any additional space beyond the input list.