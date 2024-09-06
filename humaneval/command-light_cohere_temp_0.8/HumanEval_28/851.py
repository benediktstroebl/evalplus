```python
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
```

The code defines the function `concatenate` which takes a list of strings and concatenates them into a single string. It also comes a from the strings from a list and joins them using the `join` function. The `test_concatenate` function tests the `concatenate` function by passing different inputs and asserting the expected output.