```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Returns: str
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['a', 'bc', 'a']) == 'abcaca'
test_concatenate()
```