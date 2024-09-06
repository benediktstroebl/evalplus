```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings))

# Test cases
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The function concatenate takes a list of strings as input and returns the concatenated string. The test_concatenate function tests the function with various inputs and asserts that the output is correct.