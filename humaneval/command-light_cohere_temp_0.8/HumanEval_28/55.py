```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([1,2,3]) == '123'
```

This code defines a `concatenate` function that takes a list of strings as input and returns the concatenated result as a single string. It then defines a test_concatenate function with a series of assertions that test the correctness of the `concatenate` function with different inputs.