```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abca'
    assert concatenate([1,2,3]) == '123'
```
The function `concatenate` takes a list of strings and returns a single concatenated string. The `test_concatenate` function tests the `concatenate` function with a variety of inputs and ensures that the function works correctly.