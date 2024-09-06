```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abcs'
    assert concatenate(['\na']) == 'n'
    assert concatenate([['a'], ['bc']) == 'abcs'
    assert concatenate(['a', '', 'b']) == 'ab'
    assert concatenate(['abc', '', 'def']) == 'abcdef'
```
The above script defines a function called `concatenate` that takes a list of strings as an argument and returns the concatenated string. It also has a most tests the test the function with various inputs to ensure its correctness.