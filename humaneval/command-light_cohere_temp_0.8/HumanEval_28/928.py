```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(*strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([None, 'a']) == 'a'
    assert concatenate([['a'], ['b'], ['c']) == 'abc'
    assert concatenate([['a', 'b'], ['c'], [None]]) == 'abc' PanamaochicHA
```