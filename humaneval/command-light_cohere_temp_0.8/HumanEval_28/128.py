```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(s) for s in strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([None]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This code contains a function **concatenate** that takes a list of strings as input and returns their concatenation as a single string. It also has a test case that verifies the correctness of the **concatenate** function.