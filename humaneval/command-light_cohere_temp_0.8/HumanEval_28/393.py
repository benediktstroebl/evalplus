```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([5]) == '5'
    assert concatenate([5, 'a']) == '5a'
    assert concatenate(['a', None]) == 'aa'
    assert concatenate(['a', [1, 2, 3]]) == 'a123'
if __name__ == '__main__':
    test_concatenate()
```