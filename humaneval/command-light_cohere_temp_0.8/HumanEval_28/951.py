```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    """ Test the concatenate function with various input strings """
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
    assert concatenate(['abc', '123']) == '123abc'
test_concatenate()
```