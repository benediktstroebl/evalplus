```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return the result.
    Example the required list of strings
    """
    return ''.join(''.join(strings))
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The function `concatenate` takes a list of strings and returns a new string with the strings concatenated. The function passes all corresponding tests. The test_concatenate function checks if the `concatenate` function works correctly with different inputs.