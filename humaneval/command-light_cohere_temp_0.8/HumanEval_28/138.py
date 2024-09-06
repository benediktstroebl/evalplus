```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""  
    return ''.join([s + ' ' for s in strings])

# Tests
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided Python code defines a function `concatenate` that takes a list of strings as input and returns a concatenated string by joining the strings together with spaces. The `test_concatenate` function contains unit tests for the `concatenate` function.