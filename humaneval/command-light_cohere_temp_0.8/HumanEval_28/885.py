```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.joinjoin(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([1,2,3]) == '123'
    assert concatenate(['text', 1, 2, 3]) == 'text123'
```
This Python script contains a `concatenate` function that takes a list of strings as an argument and concatenates them into a single string. The `test_concatenate` function contains a series of tests that verify the correctness of the `concatenate` function by passing various input strings and checking the output against the expected results.