```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The `concatenate` function takes a list of strings as input and concatenates them into a single string, passing the tests in the `test_concatenate` function.