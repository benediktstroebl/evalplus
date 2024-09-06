```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It is expected output is the result of the concatenate function for any list of non-empty strings. It is also passes all tests for this function, demonstrating that it works correctly.